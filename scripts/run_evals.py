#!/usr/bin/env python3
"""Run a seat's test cases with Claude Code's `claude plugin eval`.

The test cases live in evals/<seat>/ at the repository root, so the published
plugin holds only the skills. This script copies a seat and its cases into
dist/eval-runs/<seat>/ (gitignored) and runs `claude plugin eval` on that copy.
Results from earlier runs in dist/eval-runs/<seat>/evals/results/ are kept.

These are real, billed model runs.

    python3 scripts/run_evals.py the-human-cto -- --allow-tools Write,Edit,Bash
    python3 scripts/run_evals.py --all -- --runs 1
    python3 scripts/run_evals.py the-human-cfo --build-only   # just build the copy

Everything after `--` goes to `claude plugin eval` unchanged.
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "plugins" / "the-human-c-suite" / "skills"
EVALS_DIR = ROOT / "evals"
BUILD_DIR = ROOT / "dist" / "eval-runs"


def build(seat: str) -> Path:
    """Copy the seat and its cases into BUILD_DIR/<seat>, keeping earlier results."""
    target = BUILD_DIR / seat
    if target.exists():
        for child in target.iterdir():
            if child.name == "evals":
                for case in child.iterdir():
                    if case.name != "results":
                        shutil.rmtree(case) if case.is_dir() else case.unlink()
            else:
                shutil.rmtree(child) if child.is_dir() else child.unlink()
    target.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SKILLS_DIR / seat, target, dirs_exist_ok=True)
    shutil.copytree(EVALS_DIR / seat, target / "evals", dirs_exist_ok=True)
    return target


def main() -> int:
    argv = sys.argv[1:]
    extra: list[str] = []
    if "--" in argv:
        split = argv.index("--")
        argv, extra = argv[:split], argv[split + 1:]

    seats = sorted(p.name for p in EVALS_DIR.iterdir() if p.is_dir() and (SKILLS_DIR / p.name).is_dir())
    parser = argparse.ArgumentParser(description="Run a seat's test cases with `claude plugin eval`.")
    parser.add_argument("seat", nargs="*", metavar="SEAT", help=f"one or more of: {', '.join(seats)}")
    parser.add_argument("--all", action="store_true", help="run every seat")
    parser.add_argument("--build-only", action="store_true", help="build the copies and print their paths")
    args = parser.parse_args(argv)

    chosen = seats if args.all else args.seat
    if not chosen:
        parser.error("name a seat or pass --all")
    unknown = [s for s in chosen if s not in seats]
    if unknown:
        parser.error(f"unknown seat {', '.join(unknown)}; choose from {', '.join(seats)}")

    status = 0
    for seat in chosen:
        target = build(seat)
        print(f"{seat}: {target.relative_to(ROOT)}")
        if args.build_only:
            continue
        result = subprocess.run(["claude", "plugin", "eval", str(target), *extra], cwd=ROOT)
        status = status or result.returncode
    return status


if __name__ == "__main__":
    sys.exit(main())
