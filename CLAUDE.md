# CLAUDE.md — AI Security Brief

## Draft Posting Status

When starting a conversation about this project, check `drafts/` for unposted items:

1. Scan all `.md` files in `drafts/` for YAML frontmatter
2. Check `posted_en` and `posted_kr` fields
3. If any are `false`, notify the user at the start of your response:
   - Example: "Note: `brief_2026-03-04.md` has not been posted yet (EN: ✗, KR: ✗)"
4. You can also run `python3 scripts/status.py` for a full report

## Frontmatter Format

```yaml
---
type: brief          # brief | deep-dive | incident
date: 2026-03-04     # YYYY-MM-DD
posted_en: false     # true after EN is published to Threads
posted_kr: false     # true after KR quote-post is published
---
```

## Key Conventions

- Draft files live in `drafts/`, published posts move to `posted/`
- Each draft contains EN and KR versions separated by `---`
- After posting, update the corresponding `posted_en`/`posted_kr` to `true`
- Use `scripts/draft_stub.py` to create new drafts (includes frontmatter automatically)
