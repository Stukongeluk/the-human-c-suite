#!/usr/bin/env python3
"""Validate plugin metadata, shared references, and skill manifests.

Checks:
  1. Shared files and blocks are in sync (same check as sync_shared.py --check).
  2. .claude-plugin/marketplace.json and shared/manifest.json are valid JSON.
  3. Every skill under skills/ has a SKILL.md with required frontmatter fields
     and a metadata.version matching marketplace.json.
  4. Optional --tag vX.Y.Z matches the marketplace.json version.

Usage:
    python3 scripts/validate.py
    python3 scripts/validate.py --tag v1.5.0
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
MANIFEST = ROOT / "shared" / "manifest.json"
SKILLS_DIR = ROOT / "skills"


def parse_frontmatter(path: Path) -> dict:
    """Parse simple YAML frontmatter (top-level scalars and one-level nested maps)."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML frontmatter delimited by ---")

    data: dict = {}
    current_map: str | None = None

    for raw_line in match.group(1).splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith("  ") and current_map is not None:
            key, sep, val = raw_line.strip().partition(":")
            if not sep:
                raise ValueError(f"invalid nested frontmatter line: {raw_line!r}")
            data[current_map][key.strip()] = val.strip().strip('"').strip("'")
        else:
            key, sep, val = raw_line.partition(":")
            if not sep:
                raise ValueError(f"invalid frontmatter line: {raw_line!r}")
            key = key.strip()
            val = val.strip()
            if val == "":
                data[key] = {}
                current_map = key
            else:
                data[key] = val.strip('"').strip("'")
                current_map = None

    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the-human-c-suite repository.")
    parser.add_argument("--tag", help="Verify version matches this git tag (e.g. v1.5.0)")
    args = parser.parse_args()

    errors: list[str] = []

    # 1. Shared files sync check
    sync_result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "sync_shared.py"), "--check"],
        capture_output=True,
        text=True,
    )
    if sync_result.returncode != 0:
        msg = (sync_result.stdout + sync_result.stderr).strip()
        errors.append(f"shared sync check failed:\n{msg}")

    # 2. JSON files
    try:
        marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{MARKETPLACE.relative_to(ROOT)}: invalid JSON ({exc})")
        marketplace = None

    try:
        json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{MANIFEST.relative_to(ROOT)}: invalid JSON ({exc})")

    plugin_version: str | None = None
    if isinstance(marketplace, dict):
        plugins = marketplace.get("plugins")
        if not isinstance(plugins, list) or not plugins:
            errors.append(".claude-plugin/marketplace.json: missing non-empty 'plugins' array")
        else:
            plugin_version = plugins[0].get("version")
            if not plugin_version or not re.match(r"^\d+\.\d+\.\d+$", str(plugin_version)):
                errors.append(
                    f".claude-plugin/marketplace.json: invalid semver version {plugin_version!r}"
                )

    # 3. Validate each skill
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        errors.append("skills/: no skill directories found")

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        rel = skill_md.relative_to(ROOT)
        if not skill_md.exists():
            errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
            continue

        try:
            fm = parse_frontmatter(skill_md)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue

        if fm.get("name") != skill_dir.name:
            errors.append(f"{rel}: frontmatter name {fm.get('name')!r} != folder {skill_dir.name!r}")
        if not fm.get("description"):
            errors.append(f"{rel}: missing 'description'")
        if not fm.get("license"):
            errors.append(f"{rel}: missing 'license'")

        meta = fm.get("metadata")
        if not isinstance(meta, dict):
            errors.append(f"{rel}: missing 'metadata' section")
        else:
            skill_ver = meta.get("version")
            if not skill_ver:
                errors.append(f"{rel}: missing metadata.version")
            elif plugin_version and skill_ver != plugin_version:
                errors.append(
                    f"{rel}: metadata.version {skill_ver!r} != marketplace.json {plugin_version!r}"
                )

    # 4. Optional tag match
    if args.tag:
        tag_version = args.tag.lstrip("v")
        if plugin_version and tag_version != plugin_version:
            errors.append(
                f"tag {args.tag!r} does not match marketplace.json version {plugin_version!r}"
            )

    if errors:
        print("Validation failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        f"Validation passed: {len(skill_dirs)} skills at v{plugin_version}, "
        "shared references in sync."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
