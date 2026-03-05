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
5. **Post** — publish EN to Threads, then quote-post with KR version; update frontmatter to `true`
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

#### 번역투 방지 규칙

KR 버전에서 가장 흔한 실수는 영어 구조를 그대로 옮기는 것. 아래 규칙을 반드시 따를 것:

| 하지 말 것 (번역투) | 할 것 (자연스러운 한국어) |
|---|---|
| "조 단위 기업 셋. 같은 보안 설계 하나." | "Apple, Meta, Google. 셋 다 같은 곳을 보고 있어요." |
| "커스텀 실리콘. Stateless 처리. 저장 없음." | "자체 칩 서버에서 돌리고, 끝나면 바로 지워요." |
| "검증 가능한 신뢰" (verifiable trust 직역) | "'우리도 못 봅니다'를 얼마나 증명할 수 있느냐" |

- **영어 문장을 한국어 단어로 바꾸는 게 아니라, 같은 사실을 한국어로 새로 설명하는 것.**
- 누군가한테 말로 설명한다고 생각하고 쓸 것. "이거 뭔데?" 라고 물어봤을 때 대답하는 톤.
- 영어에서 짧은 문장 나열이 멋있다고 한국어에서도 그런 건 아님. 한국어는 자연스럽게 이어 쓰는 게 더 읽힘.

### Draft file format

Each draft file starts with YAML frontmatter tracking posting status, followed by both versions separated by `---`:

```yaml
---
type: brief
date: 2026-03-04
posted_en: false
posted_kr: false
---

[AI Security Brief] 2026-03-04        ← EN block

... English content ...

---

[AI 보안 브리프] 2026-03-04           ← KR block (quote post)

... Korean content ...
```

- `type`: `brief` | `deep-dive` | `incident`
- `date`: `YYYY-MM-DD`
- `posted_en` / `posted_kr`: set to `true` after publishing each version

### Posting status

Check which drafts haven't been posted yet:

```bash
python3 scripts/status.py
```

Output example:
```
Posting Status
  brief_2026-03-04.md — EN: ✗  KR: ✗
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
HOOK — 1-2 short lines that frame the story. Make the reader stop scrolling.

[AI Security Brief] Topic Label

1. HEADLINE
Short punchy line.
Another detail on its own line.
(source, YYYY-MM-DD)

2. HEADLINE
Short punchy line.
Another detail on its own line.
(source, YYYY-MM-DD)

3. HEADLINE
Short punchy line.
Another detail on its own line.
(source, YYYY-MM-DD)

Insight: one or two sentences — sharp, security-angled, connects the dots.
```

### Threads formatting rules

- **Hook first.** The `[AI Security Brief]` tag is not a hook. Start with 1-2 lines that frame why this matters.
- **Topic label, not date.** Use `[AI Security Brief] Confidential Inference` — not `[AI Security Brief] 2026-03-04`. Date lives in frontmatter only.
- **One idea per line.** Threads readers scroll with their thumb. Line breaks > long sentences.
- **Each news item = headline + 2-3 short lines.** Don't cram everything into one sentence.
- **Security angle in Insight.** Use verifiable trust, attack surface, threat model, trust boundary — not just "privacy" or "trend."

### Accuracy rules

- **Use the vendor's own language.** If Apple says "no user data retention," don't paraphrase to "no persistent storage" (implies no storage hardware). Match official terminology.
- **Don't overstate sourcing.** If a specific product/feature isn't prominently mentioned in official docs, don't name it as a key point. Generalize instead.
- **Editorializing vs. facts.** Clearly separate. "Similar pattern to Apple" is safe. "Straight from Apple's playbook" is editorial — avoid in factual lines.

Example:

```
Three tech giants.
One converging security thesis.

[AI Security Brief] Confidential Inference

1. Apple Private Cloud Compute
Custom Apple silicon.
Stateless computation.
No user data retention — deleted after every response.
Verifiable transparency + bounty-backed research.
(Apple Security Research, 2024-06-10)

2. Meta Private Processing
WhatsApp AI features run inside Confidential VMs.
Requests are end-to-end encrypted.
Even Meta cannot access message content during processing.
(Meta Engineering Blog, 2025-04-29)

3. Google Private AI Compute
Cloud Gemini inference inside hardware-rooted TEEs.
Remote attestation ensures verifiable execution.
Third-party IP-blinding relays in a similar pattern to Apple.
(Google Blog, 2025-11-11)

Insight: The next AI moat isn't model capability — it's verifiable trust. When all three design systems where operators cannot access user data even in principle, that's not a feature. That's the new baseline for AI security.
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
- [ ] Hook exists before the date tag — would you stop scrolling?
- [ ] Each news item uses short lines with line breaks, not one long sentence
- [ ] Insight uses security-specific framing (verifiable trust, attack surface, threat model)
- [ ] Korean rewrite reads naturally — sounds like explaining to someone, not translating
- [ ] Korean avoids 번역투: no word-for-word structure mirroring from EN
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
