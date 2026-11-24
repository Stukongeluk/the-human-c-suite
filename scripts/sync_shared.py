#!/usr/bin/env python3
"""Keep the reference files that several skills share identical.

Each skill folder must work on its own (people install one skill as a zip),
so shared guidance is copied into every skill that uses it. The canonical
copies live in shared/. This script copies them into the skills and fills
the marked blocks inside evidence files.

    python3 scripts/sync_shared.py          # update the skills
    python3 scripts/sync_shared.py --check  # exit 1 if anything is out of date
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
SKILLS = ROOT / "plugins" / "the-human-c-suite" / "skills"


def main() -> int:
    check = "--check" in sys.argv
    manifest = json.loads((SHARED / "manifest.json").read_text())
    stale = []

    for name, skills in manifest["files"].items():
        source = (SHARED / name).read_text()
        for skill in skills:
            target = SKILLS / skill / "references" / name
            if not target.exists() or target.read_text() != source:
                stale.append(str(target.relative_to(ROOT)))
                if not check:
                    target.write_text(source)

    for block, targets in manifest["blocks"].items():
        body = (SHARED / "blocks" / f"{block}.md").read_text().rstrip() + "\n"
        pattern = re.compile(
            rf"(<!-- shared:{re.escape(block)} -->\n).*?(<!-- /shared:{re.escape(block)} -->)",
            re.DOTALL,
        )
        for rel in targets:
            target = SKILLS / rel
            text = target.read_text()
            if not pattern.search(text):
                print(f"missing block '{block}' in {rel}", file=sys.stderr)
                return 1
            new = pattern.sub(lambda m: m.group(1) + body + m.group(2), text)
            if new != text:
                stale.append(rel)
                if not check:
                    target.write_text(new)

    if stale:
        print(("Out of date:\n  " if check else "Updated:\n  ") + "\n  ".join(stale))
        return 1 if check else 0
    print("All shared files are in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
