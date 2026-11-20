"""Run The Human C-Suite eval cases on Gemini through the Antigravity CLI (agy).

Usage (from the repository root):
    python benchmarks/gemini-v1.3/run_agy.py [--workers 3] [--out <folder>]

Each run gets a fresh, neutrally named workspace outside the repository. With the skill, the
seat is copied into <workspace>/.agents/skills/<seat>/ (without its evals folder) and invoked
as /<seat>; without the skill, the workspace is empty. Every run uses the same short note after
the user's message, so both setups get identical instructions apart from the skill.
Results land in <out>/results/<model>/<case>/<config>/run-N/ with reply.md, any documents the
agent wrote, the stream-json events and timing.json. Grading is done separately (see README.md).
"""
import argparse, json, os, re, shutil, subprocess, tempfile, time, uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CASES = {
    "ceo-leaders-first-cut": "the-human-ceo",
    "ceo-board-overrules": "the-human-ceo",
    "ceo-germany-no-works-council": "the-human-ceo",
    "cpto-sweden-support-selection": "the-human-cpto",
    "cpto-pm-sales-promise": "the-human-cpto",
    "cto-employee-ranking-dashboard": "the-human-cto",
    "cto-failed-migration-blame": "the-human-cto",
}
MODELS = ["gemini-4-neon-medium", "gemini-4-hydrogen-medium"]
CONFIGS = ["with_skill", "without_skill"]
RUNS = 2
# Headless mode can't ask for permission, and an agent whose first move is to list its folder
# otherwise ends the run with no answer. Allow read-only folder listings and nothing else.
# On Windows, commands with arguments need a regex rule (each token is matched separately).
SETTINGS = {"permissions": {"allow": [
    "command(Get-ChildItem)", "command(regex:Get-ChildItem .*)", "command(ls)", "command(regex:ls .*)",
    "command(dir)", "command(regex:dir .*)", "command(pwd)", "command(Get-Location)"]}}
NOTE = ("\n\n(Answer as you would to this person. Don't ask clarifying questions first. "
        "If you also write a separate document for them, save it as a .md file in the current folder.)")


def agy_path():
    found = shutil.which("agy")
    if found:
        return found
    local = Path(os.environ.get("LOCALAPPDATA", "")) / "agy" / "bin" / "agy.exe"
    return str(local) if local.exists() else "agy"


def prompt_of(case):
    text = (REPO / "skills" / CASES[case] / "evals" / case / "prompt.md").read_text(encoding="utf-8")
    return re.sub(r"^---.*?---\s*", "", text, flags=re.S).strip()


def run_one(job, out_root, ws_root, agy, settings_file):
    model, case, cfg, n = job
    out = out_root / "results" / model / case / cfg / f"run-{n}"
    if (out / "reply.md").exists():
        return f"skip {model}/{case}/{cfg}/run-{n}"
    out.mkdir(parents=True, exist_ok=True)
    seat = CASES[case]
    for attempt in (1, 2):
        ws = ws_root / uuid.uuid4().hex[:12]
        ws.mkdir(parents=True)
        if cfg == "with_skill":
            shutil.copytree(REPO / "skills" / seat, ws / ".agents" / "skills" / seat, ignore=shutil.ignore_patterns("evals"))
            prompt = f"/{seat} {prompt_of(case)}{NOTE}"
        else:
            prompt = f"{prompt_of(case)}{NOTE}"
        t0 = time.time()
        with open(out / "events.jsonl", "w", encoding="utf-8") as fo, open(out / "stderr.txt", "w", encoding="utf-8") as fe:
            rc = subprocess.run([agy, "-p", prompt, "--model", model, "--output-format", "stream-json",
                                 "--mode", "accept-edits", "--print-timeout", "900s", "--settings", str(settings_file)],
                                cwd=ws, stdout=fo, stderr=fe, stdin=subprocess.DEVNULL).returncode
        wall = time.time() - t0
        result = init = None
        for line in (out / "events.jsonl").read_text(encoding="utf-8").splitlines():
            try:
                ev = json.loads(line)
            except ValueError:
                continue
            if ev.get("event") == "init":
                init = ev.get("init")
            elif ev.get("event") == "result":
                result = ev.get("result")
        if result and result.get("status") == "SUCCESS" and (result.get("response") or "").strip():
            break
        if attempt == 1:
            time.sleep(30)
    (out / "reply.md").write_text((result or {}).get("response", ""), encoding="utf-8")
    docs = []
    for f in ws.rglob("*.md"):
        if ".agents" not in f.parts:
            shutil.copy(f, out / f.name)
            docs.append(f.name)
    usage = (result or {}).get("usage", {})
    (out / "timing.json").write_text(json.dumps({
        "total_tokens": usage.get("total_tokens"), "usage": usage,
        "duration_seconds": (result or {}).get("duration_seconds"), "wall_seconds": round(wall, 1),
        "status": (result or {}).get("status"), "rc": rc, "attempts": attempt,
        "expanded_commands": (init or {}).get("expanded_commands"), "documents": docs,
        "denied_actions": (result or {}).get("denied_actions"),
    }, indent=1), encoding="utf-8")
    return f"{model}/{case}/{cfg}/run-{n}: {(result or {}).get('status')} {usage.get('total_tokens')} tokens, {wall:.0f}s"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--out", default=str(Path(tempfile.gettempdir()) / "agy-c-suite-bench"))
    a = ap.parse_args()
    out_root = Path(a.out)
    ws_root = out_root / "ws"
    agy = agy_path()
    out_root.mkdir(parents=True, exist_ok=True)
    settings_file = out_root / "agy-settings.json"
    settings_file.write_text(json.dumps(SETTINGS, indent=1), encoding="utf-8")
    jobs = [(m, c, cfg, n) for n in range(1, RUNS + 1) for m in MODELS for c in CASES for cfg in CONFIGS]
    print(f"{len(jobs)} runs, {a.workers} at a time, results in {out_root}", flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        for msg in ex.map(lambda j: run_one(j, out_root, ws_root, agy, settings_file), jobs):
            print(time.strftime("%H:%M:%S"), msg, flush=True)
