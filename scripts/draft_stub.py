#!/usr/bin/env python3
"""Create a draft stub file for AI Security Brief."""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

DRAFTS_DIR = Path(__file__).resolve().parent.parent / "drafts"

TEMPLATES = {
    "brief": "[AI Security Brief] {date}\n\n1. TODO — headline and summary (source, date)\n2. TODO — headline and summary (source, date)\n3. TODO — headline and summary (source, date)\n\nInsight: TODO\n",
    "deep-dive": "[AI Security Deep Dive] {date} — TODO_TITLE\n\nSource: TODO_LINK (author, date)\n\n## Summary\nTODO\n\n## Attack / Technique\nTODO\n\n## Defense / Mitigation\nTODO\n\n## Implications\nTODO\n\n## Key Takeaway\nTODO\n",
    "incident": "[AI Security Incident] {date} — TODO_NAME\n\n## What Happened\nTODO\n\n## Timeline\n- {date} — TODO\n\n## Impact\nTODO\n\n## Root Cause\nTODO\n\n## Response\nTODO\n\n## Lessons Learned\nTODO\n",
}


def main():
    parser = argparse.ArgumentParser(description="Create a draft stub file.")
    parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD format")
    parser.add_argument(
        "--type",
        required=True,
        choices=["brief", "deep-dive", "incident"],
        dest="draft_type",
        help="Draft type",
    )
    args = parser.parse_args()

    # Validate date format
    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print(f"Error: invalid date format '{args.date}', expected YYYY-MM-DD", file=sys.stderr)
        sys.exit(1)

    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)

    filename = f"{args.draft_type}_{args.date}.md"
    filepath = DRAFTS_DIR / filename

    if filepath.exists():
        print(f"Draft already exists: {filepath}")
        sys.exit(0)

    content = TEMPLATES[args.draft_type].format(date=args.date)
    filepath.write_text(content)
    print(f"Created: {filepath}")


if __name__ == "__main__":
    main()
