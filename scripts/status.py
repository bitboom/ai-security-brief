#!/usr/bin/env python3
"""Report posting status of drafts by reading YAML frontmatter."""

import sys
from pathlib import Path

DRAFTS_DIR = Path(__file__).resolve().parent.parent / "drafts"


def parse_frontmatter(text):
    """Parse YAML frontmatter between --- delimiters. Returns dict or None."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    end = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            end = i
            break
    if end is None:
        return None
    meta = {}
    for line in lines[1:end]:
        if ":" in line:
            key, _, value = line.partition(":")
            value = value.strip()
            if value == "true":
                value = True
            elif value == "false":
                value = False
            meta[key.strip()] = value
    return meta


def main():
    if not DRAFTS_DIR.exists():
        print("No drafts/ directory found.")
        sys.exit(0)

    md_files = sorted(DRAFTS_DIR.glob("*.md"))
    if not md_files:
        print("No draft files found.")
        sys.exit(0)

    unposted = []
    for path in md_files:
        meta = parse_frontmatter(path.read_text())
        if meta is None:
            continue
        en = meta.get("posted_en")
        kr = meta.get("posted_kr")
        if en is False or kr is False:
            unposted.append((path.name, en, kr))

    if not unposted:
        print("All drafts posted!")
        sys.exit(0)

    print("Posting Status")
    for name, en, kr in unposted:
        parts = []
        if en is not None:
            parts.append(f"EN: {'✓' if en else '✗'}")
        if kr is not None:
            parts.append(f"KR: {'✓' if kr else '✗'}")
        print(f"  {name} — {'  '.join(parts)}")


if __name__ == "__main__":
    main()
