#!/usr/bin/env python3
"""Validate plugin metadata, shared references, and skill manifests.

Checks:
  1. Shared files and blocks are in sync (same check as sync_shared.py --check).
  2. .claude-plugin/marketplace.json, the plugin's .claude-plugin/plugin.json and
     shared/manifest.json are valid JSON; the marketplace points at the plugin
     folder and both carry the same name and version.
  3. The plugin folder meets the Claude plugin directory's file rules: a README
     of at least 40 words outside code blocks, a LICENSE, at most 512 files,
     only text or image files, nothing but images over 256 KiB, no OS clutter
     and no test cases (those live in evals/ at the repository root); every
     MCP server in .mcp.json is a remote https server without credentials.
  4. Every skill in the plugin has a SKILL.md with required frontmatter fields
     and a metadata.version matching the plugin version, and every folder in
     evals/ belongs to a skill.
  5. Optional --tag vX.Y.Z matches the plugin version.

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
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
MANIFEST = ROOT / "shared" / "manifest.json"
PLUGIN_DIR = ROOT / "plugins" / "the-human-c-suite"
PLUGIN_JSON = PLUGIN_DIR / ".claude-plugin" / "plugin.json"
SKILLS_DIR = PLUGIN_DIR / "skills"
EVALS_DIR = ROOT / "evals"

# The Claude plugin directory holds a submission for a reviewer when the plugin
# folder breaks these limits (see the plugin pre-submission checklist).
MAX_PLUGIN_FILES = 512
MAX_FILE_BYTES = 256 * 1024
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".txt", ".csv", ".svg"}
CLUTTER = {".DS_Store", "Thumbs.db", "desktop.ini", "__MACOSX"}


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

    try:
        plugin = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{PLUGIN_JSON.relative_to(ROOT)}: missing or invalid JSON ({exc})")
        plugin = None

    plugin_version: str | None = None
    plugin_rel = PLUGIN_JSON.relative_to(ROOT).as_posix()
    if isinstance(plugin, dict):
        plugin_version = plugin.get("version")
        if not plugin_version or not re.match(r"^\d+\.\d+\.\d+$", str(plugin_version)):
            errors.append(f"{plugin_rel}: invalid semver version {plugin_version!r}")
        name = str(plugin.get("name", ""))
        if not re.match(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$", name):
            errors.append(f"{plugin_rel}: name {name!r} must be lowercase letters, digits and hyphens")
        for key in ("description", "author", "license"):
            if not plugin.get(key):
                errors.append(f"{plugin_rel}: missing {key!r}")

    if isinstance(marketplace, dict):
        plugins = marketplace.get("plugins")
        if not isinstance(plugins, list) or not plugins:
            errors.append(".claude-plugin/marketplace.json: missing non-empty 'plugins' array")
        elif isinstance(plugin, dict):
            entry = plugins[0]
            source = str(entry.get("source", "")).rstrip("/")
            expected = "./" + PLUGIN_DIR.relative_to(ROOT).as_posix()
            if source != expected:
                errors.append(f".claude-plugin/marketplace.json: source {source!r} != {expected!r}")
            for key in ("name", "version"):
                if entry.get(key) != plugin.get(key):
                    errors.append(
                        f".claude-plugin/marketplace.json: {key} {entry.get(key)!r} != "
                        f"plugin.json {plugin.get(key)!r}"
                    )

    # 3. Plugin folder rules of the Claude plugin directory
    readme = PLUGIN_DIR / "README.md"
    if not readme.exists():
        errors.append(f"{PLUGIN_DIR.relative_to(ROOT)}: missing README.md")
    else:
        prose = re.sub(r"```.*?```", " ", readme.read_text(encoding="utf-8"), flags=re.DOTALL)
        words = len(re.findall(r"\w+", prose))
        if words < 40:
            errors.append(f"{readme.relative_to(ROOT)}: {words} words outside code blocks; needs 40")
    if not (PLUGIN_DIR / "LICENSE").exists():
        errors.append(f"{PLUGIN_DIR.relative_to(ROOT)}: missing LICENSE")

    plugin_files = [p for p in PLUGIN_DIR.rglob("*") if p.is_file()]
    if len(plugin_files) > MAX_PLUGIN_FILES:
        errors.append(
            f"{PLUGIN_DIR.relative_to(ROOT)}: {len(plugin_files)} files; "
            f"the plugin directory holds more than {MAX_PLUGIN_FILES} for a reviewer"
        )
    for path in plugin_files:
        rel_path = path.relative_to(ROOT)
        parts = path.relative_to(PLUGIN_DIR).parts
        if any(part in CLUTTER for part in parts):
            errors.append(f"{rel_path}: OS clutter file")
        elif "evals" in parts:
            errors.append(f"{rel_path}: test cases belong in evals/ at the repository root")
        elif path.suffix in IMAGE_SUFFIXES:
            continue
        elif path.suffix not in TEXT_SUFFIXES and path.name != "LICENSE":
            errors.append(f"{rel_path}: not a text or image file")
        elif path.stat().st_size > MAX_FILE_BYTES:
            errors.append(f"{rel_path}: {path.stat().st_size // 1024} KiB; keep files under 256 KiB")

    mcp_file = PLUGIN_DIR / ".mcp.json"
    if mcp_file.exists():
        mcp_rel = mcp_file.relative_to(ROOT)
        try:
            servers = json.loads(mcp_file.read_text(encoding="utf-8")).get("mcpServers", {})
        except Exception as exc:
            errors.append(f"{mcp_rel}: invalid JSON ({exc})")
            servers = {}
        for name, server in servers.items():
            url = server.get("url")
            if server.get("type") != "http" or url is None:
                errors.append(f"{mcp_rel}: {name!r} must be a remote server with type 'http' and a url")
            elif url and not url.startswith("https://"):
                errors.append(f"{mcp_rel}: {name!r} url must be https:// (or empty for a server without a fixed address)")
            if server.get("headers") or server.get("command"):
                errors.append(f"{mcp_rel}: {name!r} must not carry headers or a local command")
            host = (urlparse(url).hostname or "").lower() if url else ""
            if re.search(r"(^|\.)(claude\.(com|ai)|anthropic\.com)$", host):
                errors.append(
                    f"{mcp_rel}: {name!r} uses an Anthropic-hosted address ({host}); the plugin "
                    "directory accepts those only from verified organisations"
                )
            if server.get("oauth") or server.get("authServerMetadataUrl"):
                errors.append(f"{mcp_rel}: {name!r} must not set its own sign-in (oauth, clientId or authServerMetadataUrl)")

    # 4. Validate each skill
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        errors.append(f"{SKILLS_DIR.relative_to(ROOT)}: no skill directories found")
    skill_names = {p.name for p in skill_dirs}
    if EVALS_DIR.is_dir():
        for eval_dir in sorted(p for p in EVALS_DIR.iterdir() if p.is_dir()):
            if eval_dir.name not in skill_names:
                errors.append(f"{eval_dir.relative_to(ROOT)}: no skill named {eval_dir.name!r}")

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
        elif len(str(fm["description"])) > 1024:
            errors.append(f"{rel}: description is {len(str(fm['description']))} characters; the Agent Skills limit is 1024")
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
                    f"{rel}: metadata.version {skill_ver!r} != plugin.json {plugin_version!r}"
                )

    # 5. Optional tag match
    if args.tag:
        tag_version = args.tag.lstrip("v")
        if plugin_version and tag_version != plugin_version:
            errors.append(
                f"tag {args.tag!r} does not match plugin.json version {plugin_version!r}"
            )

    if errors:
        print("Validation failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        f"Validation passed: {len(skill_dirs)} skills at v{plugin_version}, "
        f"{len(plugin_files)} files in the plugin, shared references in sync."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
