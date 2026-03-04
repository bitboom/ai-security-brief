#!/usr/bin/env python3
"""Create a draft stub file for AI Security Brief."""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

DRAFTS_DIR = Path(__file__).resolve().parent.parent / "drafts"

TEMPLATES_EN = {
    "brief": "[AI Security Brief] {date}\n\n1. TODO — punchy one-sentence summary (source, date)\n2. TODO — punchy one-sentence summary (source, date)\n3. TODO — punchy one-sentence summary (source, date)\n\nInsight: TODO — sharp, opinionated, connect the dots.\n",
    "deep-dive": "[AI Security Deep Dive] {date} — TODO_TITLE\n\nSource: TODO_LINK (author, date)\n\nTL;DR — TODO\n\nWhat it is:\nTODO\n\nHow it works:\nTODO\n\nSo what?\nTODO\n\nWhat to do about it:\nTODO\n\nBottom line:\nTODO\n",
    "incident": "[AI Security Incident] {date} — TODO_NAME\n\nWhat happened:\nTODO\n\nTimeline:\n- {date} — TODO\n\nWho got hurt:\nTODO\n\nHow it happened:\nTODO\n\nWhat they did about it:\nTODO\n\nThe lesson:\nTODO\n",
}

TEMPLATES_KR = {
    "brief": "[AI 보안 브리프] {date}\n\n1. TODO — 한 줄 요약, 간결하고 임팩트 있게 (출처, 날짜)\n2. TODO — 한 줄 요약, 간결하고 임팩트 있게 (출처, 날짜)\n3. TODO — 한 줄 요약, 간결하고 임팩트 있게 (출처, 날짜)\n\n인사이트: TODO — 날카롭고 핵심을 찌르는 한두 문장.\n",
    "deep-dive": "[AI 보안 딥다이브] {date} — TODO_제목\n\n출처: TODO_링크 (저자, 날짜)\n\nTL;DR — TODO\n\n뭔데?:\nTODO\n\n어떻게 작동해?:\nTODO\n\n그래서?:\nTODO\n\n어떻게 대응해?:\nTODO\n\n한 줄 정리:\nTODO\n",
    "incident": "[AI 보안 인시던트] {date} — TODO_사건명\n\n무슨 일이야?:\nTODO\n\n타임라인:\n- {date} — TODO\n\n피해는?:\nTODO\n\n원인이 뭐야?:\nTODO\n\n어떻게 대응했어?:\nTODO\n\n교훈:\nTODO\n",
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
    parser.add_argument(
        "--lang",
        choices=["en", "ko", "both"],
        default="en",
        help="Language: en (default), ko, or both",
    )
    args = parser.parse_args()

    # Validate date format
    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print(f"Error: invalid date format '{args.date}', expected YYYY-MM-DD", file=sys.stderr)
        sys.exit(1)

    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.lang == "ko":
        filename = f"{args.draft_type}_{args.date}_ko.md"
    else:
        filename = f"{args.draft_type}_{args.date}.md"
    filepath = DRAFTS_DIR / filename

    if filepath.exists():
        print(f"Draft already exists: {filepath}")
        sys.exit(0)

    # Build frontmatter
    frontmatter_lines = [
        "---",
        f"type: {args.draft_type}",
        f"date: {args.date}",
    ]
    if args.lang in ("en", "both"):
        frontmatter_lines.append("posted_en: false")
    if args.lang in ("ko", "both"):
        frontmatter_lines.append("posted_kr: false")
    frontmatter_lines.append("---")
    frontmatter = "\n".join(frontmatter_lines) + "\n\n"

    if args.lang == "en":
        content = frontmatter + TEMPLATES_EN[args.draft_type].format(date=args.date)
    elif args.lang == "ko":
        content = frontmatter + TEMPLATES_KR[args.draft_type].format(date=args.date)
    else:  # both
        en = TEMPLATES_EN[args.draft_type].format(date=args.date)
        kr = TEMPLATES_KR[args.draft_type].format(date=args.date)
        content = frontmatter + en + "\n---\n\n" + kr

    filepath.write_text(content)
    print(f"Created: {filepath}")


if __name__ == "__main__":
    main()
