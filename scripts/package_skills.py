#!/usr/bin/env python3
"""Package each skill and the full C-Suite into clean, upload-ready zip archives.

Excludes evals/ and OS/Python clutter so the archives can be uploaded directly
to Claude apps (Customize > Skills) or unzipped into an agent's skills folder
(such as .agents/skills/ in Antigravity or ~/.claude/skills/ in Claude Code).

Usage:
    python3 scripts/package_skills.py                # writes into dist/
    python3 scripts/package_skills.py --out build/
"""
import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
SKILLS_DIR = ROOT / "skills"

EXCLUDED_DIRS = {"evals", "__pycache__"}
EXCLUDED_FILES = {".DS_Store", "Thumbs.db"}


def read_version() -> str:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    return str(data["plugins"][0]["version"])


def iter_skill_files(skill_dir: Path):
    """Yield (disk_path, archive_path) pairs in sorted order, excluding evals/."""
    for path in sorted(skill_dir.rglob("*")):
        if path.is_dir():
            continue
        rel_parts = path.relative_to(skill_dir).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        if path.name in EXCLUDED_FILES or path.suffix in {".pyc", ".pyo"}:
            continue
        arcname = Path(skill_dir.name, *rel_parts).as_posix()
        yield path, arcname


def write_zip(zip_path: Path, entries: list[tuple[Path, str]]) -> None:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for disk_path, arcname in entries:
            zf.write(disk_path, arcname)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Build release zip archives for all skills.")
    parser.add_argument("--out", default="dist", help="Output directory (default: dist)")
    parser.add_argument("--version", help="Override version string (default: marketplace.json)")
    args = parser.parse_args()

    version = (args.version or read_version()).lstrip("v")
    out_dir = Path(args.out)
    if not out_dir.is_absolute():
        out_dir = ROOT / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        print("No skill directories found under skills/", file=sys.stderr)
        return 1

    created: list[Path] = []
    bundle_entries: list[tuple[Path, str]] = []

    for skill_dir in skill_dirs:
        entries = list(iter_skill_files(skill_dir))
        zip_path = out_dir / f"{skill_dir.name}-v{version}.zip"
        write_zip(zip_path, entries)
        created.append(zip_path)
        bundle_entries.extend(entries)

    bundle_path = out_dir / f"the-human-c-suite-v{version}.zip"
    write_zip(bundle_path, bundle_entries)
    created.append(bundle_path)

    checksum_lines = [f"{sha256_file(p)}  {p.name}" for p in created]
    checksums_path = out_dir / "SHA256SUMS.txt"
    checksums_path.write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")

    for path in created:
        size_kb = path.stat().st_size / 1024
        print(f"  {path.name} ({size_kb:.1f} KB)")
    print(f"  {checksums_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
