---
name: jobs-to-be-done
description: >-
  Systematically uncover customer jobs, pains, and gains using the
  Jobs-to-be-Done framework. Use when the user mentions "jobs to be done",
  "JTBD", "customer jobs", "unmet needs", "pains and gains", "value
  proposition canvas", "switch interviews", "outcome-driven innovation",
  "desired outcomes", or asks why customers hire or fire a product. Also
  trigger when the user wants to understand what job a product solves,
  conduct customer discovery, reposition a product around needs, define
  unmet needs for a roadmap, analyze competitors through a jobs lens, or
  create messaging grounded in what customers are trying to accomplish.
  Do NOT use for general market sizing, feature prioritization without a
  customer-needs lens, competitive analysis focused on features rather
  than jobs, or persona creation based on demographics alone.
metadata:
  author: ninhnv
  version: 2.0.0
  category: product-management
---

# Jobs-to-be-Done — AI Guidance

JTBD uncovers *why* customers "hire" a product, not what features they want. Stay solution-agnostic. The goal is to surface real motivations, unmet needs, and the functional/emotional/social jobs behind any request.

---

## How to Behave

**On first use:** Ask for context before proceeding. You need at minimum: (1) who the job performer is, (2) what product/domain this is for, and (3) whether they have research or are working from assumptions.

**When research exists:** Work from it. Help structure, translate, and sharpen insights into well-formed JTBD statements.

**When no research exists:** Flag it — label all outputs as "hypothesized, needs validation." Still proceed; a hypothesis beats nothing. Recommend methods from `references/research-methods.md`.

**Output format:** Always use `template.md` as the structure. For lightweight requests: complete elements 1–4 + Approach A (Pains/Gains). For rigorous requests: also complete Approach B (Desired Outcomes). Always end with Implications.

**Quality-check everything** against `references/quality-checks.md`. Read it before generating job or outcome statements.

**Proactively catch pitfalls** from `references/pitfalls.md` — especially: solutions embedded in job statements, generic jobs, missing circumstances, and unranked pains.

---

## The Five Elements

Work through these in order. Each builds on the previous.

| # | Element | Key Rule |
| --- | --------- | ---------- |
| 1 | **Job Performer** (Who) | Name by role + context, not demographic. Distinguish performer from buyer, approver, audience. |
| 2 | **Main Job** (What) | `verb + object + clarifier`. Solution-agnostic. Stable over time. Clear "done" state. No adjectives. |
| 3 | **Emotional & Social Jobs** | Emotional: "Feel…" / "Avoid feeling…". Social: "Be seen as… by [specific audience]". Keep separate from functional job. |
| 4 | **Circumstances** (When/Where) | Min 3–5 per job. Cover: time pressure, environment, constraints, frequency. Context makes generic jobs actionable. |
| 5 | **Job Process Map** (How) | Stages: Define → Locate → Prepare → Execute → Monitor → Modify → Conclude → Share. Adapt as needed. Attach needs to each stage. |

---

## Formulation Rules (Apply Strictly)

**Job statements:** `verb + object + clarifier`

- ✓ "Coordinate tasks across a distributed team"
- ✗ "Use Slack to communicate" — solution embedded
- ✗ "Be more productive" — vague, no done state
- ✗ "Quickly manage finances" — adjective belongs in needs, not job

**Abstraction:** Ask "Why?" to go broader, "How?" to go narrower.

- Aspiration: "Be financially secure" → too broad for product scope
- Big Job: "Plan long-term retirement savings" → product strategy level
- Little Job: "Reconcile monthly expenses" → feature level
- Micro-Job: "Categorize a receipt" → UX/interaction level

**Desired Outcome statements:** `direction of change + unit of measure + object of control + clarifier`

- ✓ "Minimize the time it takes to reconcile monthly expenses"
- ✓ "Reduce the likelihood of missing a critical project dependency"
- ✗ "Make reports faster" — no structure
- ✗ "Better collaboration" — not measurable

**Opportunity score** = Importance + max(Importance − Satisfaction, 0). Scores >12 = priority targets. Scores >15 = critical.

---

## Needs: Two Approaches

**Approach A — Pains/Gains** (default):
Use for workshops, early discovery, cross-functional teams.

- Pains: Challenges, Costliness, Common Mistakes, Unresolved Problems
- Gains: Expectations, Savings, Adoption Factors, Life Improvement

**Approach B — Desired Outcomes** (higher rigor):
Use for roadmap decisions, prioritization, quantitative surveys.
Attach outcomes to each job stage. Lightweight = 15–30; thorough = 50–150.

---

## Workflow

1. **Clarify context** — Performer, main job, circumstances, current solutions (include non-obvious: spreadsheets, workarounds, doing nothing)
2. **Map the job process** — Lay out stages, note friction at each
3. **Document jobs** — Functional (main + related), emotional, social
4. **Capture needs** — Pains/Gains or Desired Outcomes per stage. Be exhaustive.
5. **Prioritize** — Rank pains by intensity × frequency. Score desired outcomes. Identify must-have gains. Segment if performers differ.
6. **Draw implications** — Product strategy, messaging, competitive positioning, what still needs validation

---

## Key Principles

- Jobs are stable; solutions change. Define at a level that transcends technology.
- Functional job first. Emotional/social jobs differentiate only after functional parity.
- Real competition is often non-obvious — workarounds, manual processes, "doing nothing."
- Depth over breadth. One well-defined job beats five vague ones.
- Never present assumptions as validated insights. Label them.

---

## Reference Files

| File | When to Read |
| ------ | ------------- |
| `template.md` | Always — use as the output structure |
| `references/quality-checks.md` | Before writing any job or outcome statements |
| `references/pitfalls.md` | When reviewing or correcting an existing analysis |
| `references/research-methods.md` | When user has no research or asks how to run interviews |
| `examples/sample.md` | When user needs worked examples to calibrate quality |
