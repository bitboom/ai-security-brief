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

## Writing Rules (MUST follow)

### EN — Threads formatting

- **Hook first.** 1-2 short lines before the `[AI Security Brief]` tag. Frame why this matters. Make the reader stop scrolling.
- **Topic label, not date.** `[AI Security Brief] Confidential Inference` — date lives in frontmatter only.
- **One idea per line.** Each news item = headline on its own line + 2-3 short detail lines. No single-sentence paragraphs stuffing everything in.
- **Security angle in Insight.** Use security language (verifiable trust, attack surface, threat model, trust boundary), not just generic privacy/trend framing.
- **Match vendor terminology.** Use the official language from vendor docs. Don't paraphrase in ways that change meaning (e.g., "no user data retention" ≠ "no persistent storage").

### KR — 번역투 방지

- **번역이 아니라 리라이트.** 영어 문장 구조를 그대로 옮기지 말 것. 같은 사실을 한국어로 새로 설명하는 것.
- **말하듯이 쓸 것.** "이거 뭔데?"라고 물어봤을 때 대답하는 톤. 누군가한테 설명한다고 생각하고 쓸 것.
- **영어식 짧은 문장 나열 금지.** 영어에서 "Custom silicon. Stateless. No storage."가 멋있어도, 한국어에서는 "자체 칩 서버에서 돌리고, 끝나면 바로 지워요"가 더 자연스러움.
- **Hook도 새로 쓸 것.** EN hook을 번역하지 말고, 한국어 독자가 멈출 만한 문장을 따로 쓸 것.
