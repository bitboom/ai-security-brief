# Scripts

Automation helpers for the AI Security Brief workflow.

## draft_stub.py

Creates a new draft file from a template.

```bash
python3 scripts/draft_stub.py --date 2026-03-04 --type brief
python3 scripts/draft_stub.py --date 2026-03-04 --type deep-dive
python3 scripts/draft_stub.py --date 2026-03-04 --type incident
```

**Arguments:**
- `--date` — date in `YYYY-MM-DD` format (required)
- `--type` — one of `brief`, `deep-dive`, `incident` (required)

**Output:** creates a file in `drafts/` named `{type}_{date}.md` with a TODO body.
