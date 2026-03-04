# AI Security Brief

## Overview

AI Security Brief is a curated series of concise, actionable security intelligence focused on artificial intelligence. It tracks emerging threats, vulnerabilities, research, and policy developments at the intersection of AI and cybersecurity — distilled into Threads-ready posts for daily consumption.

## Outputs

| Format | Cadence | Description |
|--------|---------|-------------|
| **Daily Brief** | Daily | 3 news items + editorial insight |
| **Deep Dive** | Weekly | Single paper, report, or technique analyzed in depth |
| **Incident Case** | As needed | Breakdown of a specific incident, leak, or vulnerability |

## Operating Routine

Daily workflow (~10–15 min):

1. **Collect** — scan RSS feeds, accounts, and alerts for AI security news
2. **Log** — record noteworthy items in `news/YYYY-MM-DD.md`
3. **Draft** — write a Threads-ready post in `drafts/`
4. **Review** — run the quality checklist below
5. **Post** — publish EN to Threads, then quote-post with KR version
6. **Archive** — move the draft to `posted/`

## Bilingual Posting (EN → KR)

Every post is published in two steps using Threads' **quote post** feature:

1. **Publish the English original** — the primary post
2. **Quote-post with the Korean version** — embeds the EN original so Korean readers always see both

Why quote post? Feed ordering on Threads is unpredictable. A quote post guarantees the Korean version visually includes the English original, regardless of when each appears in followers' feeds.

### Korean writing guidelines

- The KR version is a **rewrite**, not a translation. Same facts, same tone, natural Korean.
- Base register: **존댓말 (해요체)** — conversational and approachable, not stiff 합니다체.
- Technical terms: keep English with inline Korean context where needed (e.g., "프롬프트 인젝션(prompt injection)").
- Header format: EN uses `[AI Security Brief]`, KR uses `[AI 보안 브리프]`.
- Deep Dive → `[AI 보안 딥다이브]`, Incident → `[AI 보안 인시던트]`.

### Draft file format

Each draft file contains both versions separated by `---`:

```
[AI Security Brief] 2026-03-04        ← EN block

... English content ...

---

[AI 보안 브리프] 2026-03-04           ← KR block (quote post)

... Korean content ...
```

## Voice & Tone

This series is written for **Threads** — short, punchy, scroll-stopping. The guiding principles:

- **Professional but human.** You know your stuff, but you're not writing a NIST report. Think "smart colleague explaining over coffee," not "vendor whitepaper."
- **Accessible first.** A developer, PM, or curious founder should understand every post without Googling acronyms. If you must use jargon, explain it inline.
- **Witty, not try-hard.** A well-placed analogy or dry observation keeps readers engaged. Forced humor doesn't. One good line per post is plenty.
- **Threads-native.** Short paragraphs. Line breaks between ideas. No walls of text. The reader is scrolling with their thumb — respect that.
- **Confident but honest.** State what's known clearly. Flag what's uncertain. Never hype, never downplay.

### Tone Do's & Don'ts

| Do | Don't |
|----|-------|
| "Think of it as a skeleton key for LLMs" | "This is a paradigm-shifting attack vector" |
| "Reportedly" / "claims" when unconfirmed | State rumors as fact |
| Use one relatable analogy per post | Stack three metaphors in a row |
| End with a sharp, quotable insight | End with "time will tell" |
| Write like you'd text a smart friend | Write like a press release |

## Writing Format

Every Daily Brief follows this fixed structure:

```
[AI Security Brief] YYYY-MM-DD

1. HEADLINE — one-sentence summary (source, date)
2. HEADLINE — one-sentence summary (source, date)
3. HEADLINE — one-sentence summary (source, date)

Insight: one or two sentences — sharp, opinionated, connects the dots.
```

Example:

```
[AI Security Brief] 2026-03-04

1. GPT-5 jailbreak bypasses alignment filters — A prompt-injection chain slips past GPT-5's safety layer like it's not even there (Arxiv, 2026-03-03)
2. EU AI Act drops its first fines — Two facial-recognition vendors just became expensive cautionary tales (Reuters, 2026-03-04)
3. Model poisoning toolkit goes open-source — Red teamers rejoice, blue teamers update your threat models (GitHub, 2026-03-02)

Insight: New attack tooling on Monday, new regulation fines on Tuesday. 2026 is making it very clear — AI security isn't a nice-to-have anymore, it's the cost of doing business.
```

## Sourcing & Link Policy

- Always link to the **original source** (paper, advisory, official announcement), not aggregator rewrites.
- Date format: `YYYY-MM-DD`.
- Source trust tiers:
  - **Tier 1** — Peer-reviewed papers, official vendor advisories, government agencies
  - **Tier 2** — Established security outlets (Krebs, The Record, BleepingComputer), major wire services
  - **Tier 3** — Individual researchers, blogs, social media (verify before citing)

## Quality Checklist

Before posting, verify:

- [ ] All facts are sourced and dated
- [ ] Technical terms are used correctly (and explained if niche)
- [ ] Tone is sharp but not sensational — witty, not hype
- [ ] Uncertainty is marked explicitly ("reportedly", "claims", "unconfirmed")
- [ ] Links point to original sources
- [ ] Post fits the fixed format
- [ ] Would you actually stop scrolling to read this? If not, rewrite the hook
- [ ] Korean rewrite reads naturally (not translated-sounding)
- [ ] Technical terms: English preserved with Korean context where needed

## Directory Layout

```
ai-security-brief/
├── sources/          # RSS feeds, accounts to follow
├── news/             # Daily raw news clippings (YYYY-MM-DD.md)
├── drafts/           # Work-in-progress Threads posts
├── posted/           # Published posts (archived)
├── templates/        # Post format templates
├── scripts/          # Automation helpers
└── .github/          # Issue templates, workflows
```

## GitHub Projects Kanban

Use a GitHub Project board with these columns:

| Column | Description |
|--------|-------------|
| **Backlog** | Interesting topics saved for later |
| **Research** | Actively gathering sources and context |
| **Draft** | Writing in progress |
| **Review** | Quality checklist pass |
| **Ready** | Approved, waiting to post |
| **Posted** | Published and archived |

## Remote Push

To create and push the remote repository:

```bash
gh repo create ai-security-brief --public --source=. --remote=origin --push
```

Or manually:

```bash
git remote add origin https://github.com/<your-username>/ai-security-brief.git
git push -u origin main
```

## Disclaimer

AI Security Brief is provided for **informational and educational purposes only**. It does not constitute legal, compliance, or professional security advice. The author is not responsible for actions taken based on this content. Do not use any referenced techniques, tools, or methods for unauthorized or malicious purposes.
