---
name: user-story-skill
description: >-
  Systematically create INVEST-standard User Stories with comprehensive Acceptance Criteria. Use when the user mentions "user story", "acceptance criteria", "AC", "INVEST", "story splitting", "story hierarchy", or asks for help writing or reviewing user stories. Also trigger when the user wants to decompose a feature into stories, ensure testable conditions, or align stories with business value. Do NOT use for general requirements gathering, feature specifications without a user-centric focus, or technical task breakdowns that don't follow the user story format.
---

# SKILL: User Stories & Acceptance Criteria

**Trigger:** Write / draft / review / decompose / check User Stories or AC.
**Rule:** Read fully before producing any output.

---
 
## 1 · STORY FORMAT (Non-Negotiable)

```text
As a [specific Actor/Persona],
I want to [Action + Object],
so that [Value/Reason].
```

| Part | Guidance |
|------|----------|
| **WHO** (Actor) | Specific named persona — never "user", "system", or "developer". Represents how the person works, thinks, feels. One actor per story. |
| **DOES + WHAT** (Action) | Outcome-focused, implementation-free. No UI elements, no technical prescriptions. Use "I want to [do X]" — avoid "I need a [feature]". |
| **WHY** (so that) | Genuine user/business value — never a system requirement. Always present. Ask "Why?" 5× to reach true motivation. |
| **DONE WHEN** (AC) | Testable conditions confirming the story is complete. See Section 3. |

---

## 2 · INVEST (validate before every story)

| | Criterion | Check |
|-|-----------|-------|
| **I** | Independent | Stands alone; no dependency on incomplete stories |
| **N** | Negotiable | Starting point for discussion, not a locked contract |
| **V** | Valuable | Delivers real value to user or business |
| **E** | Estimable | Team can size it; if not → clarify or split |
| **S** | Small | Built + tested within one sprint (≤ 3 dev days) |
| **T** | Testable | Every AC has a clear pass/fail condition |

---

## 3 · ACCEPTANCE CRITERIA (AC)

**Format:** `Done when: [testable condition — pass/fail verifiable]`
**Prefer** "Done when" over Gherkin (Given/When/Then) — simpler to read and test.

### Must cover all of these

| Type | Rule |
|------|------|
| **Happy path** | At least one AC for the main successful flow |
| **Negative/edge flows** | `Done when: If [X], then [Y]` — at least one error/edge case |
| **Role-based** | Separate AC per role if multiple actors — only combine if buildable + testable together |
| **NFRs** | Performance, capacity, security — use exact thresholds, never vague quantifiers |
| **Design hints** | Framed as preference: `Done when: Report is exportable. (Customer prefers Excel.)` |

### NFR placement

1. In the **WHAT** clause (if it defines system behaviour)
2. In **AC** (preferred — for performance, capacity, security)
3. As its **own story** if effort is sprint-sized

### MoSCoW for AC priority

**M**ust / **S**hould / **C**ould / **W**on't — if an AC is Could/Won't, break it into a separate "Nice to Have" story rather than mixing priorities.

---

## 4 · ACTOR RULES

- Single actor, single action, single outcome per story
- If multiple roles share the same functionality: one story + role-based AC **only if** buildable AND testable together; otherwise → separate stories

---

## 5 · WHEN TO SPLIT A STORY

Split when any of these are true:

- `and` / `or` / `/` in the story statement
- AC list spans more than one sprint
- Multiple actors need separate build + test paths
- NFR effort is significant enough to own a sprint slot
- Story points = XL

**Strategies:** Part 1/2/3 · Split by actor · Split by flow (positive vs. edge) · Split by CRUD scope (Create / Edit / Delete)

---

## 6 · HIERARCHY

```text
Epic → Feature → User Story
```

- Stories must connect to a Feature; Features to an Epic
- Each story's "Why" must be **self-contained** — repeat Epic context in the story; devs work from stories, not Epics

---

## 7 · SPECIAL CASES

**API stories**

```text
As the [API name], I want to include [data] in the response,
so that [consumer] can [outcome].
```

Also define: endpoints, who pulls/publishes data, how data is used.

**Reporting stories:** WHO = person who uses the report · WHAT/AC = fields, data types · WHY = business reason

**Non-collocated teams:** Add more AC detail; supplement with SRD or mockup; link all artifacts explicitly in the story.

**Mockups:** Each mockup section → one or more stories. Developed collaboratively. Suggestion tool only — not a locked design.

---

## 8 · ANTI-PATTERNS

| ❌ Anti-Pattern | Problem | ✅ Fix |
|-----------------|---------|--------|
| "I need a [feature]" | Leads to design requirements | Use "I want to [action]" |
| "and/or/" in statement | Multiple outcomes | Split story |
| Multiple actors, one story | Can't build+test together | Separate stories |
| Prescribes UI/technical solution | Limits team creativity | Describe user goal only |
| Generic actor ("user", "system", "developer") | No empathy or end-user value | Use specific persona |
| AC list too long | Spans multiple sprints | Split story |
| Vague NFR ("more than X") | Untestable | Use exact threshold |
| Developer as actor | No end-user value | Reframe as technical task |
| Missing "so that" | Team doesn't know the why | Always include value clause |

---

## 9 · OUTPUT FORMAT

```text
## User Story
**Title:** [Short descriptive title]

As a [Actor],
I want to [Action + Object],
so that [Value].

## Acceptance Criteria
Done when: [positive condition]
Done when: [positive condition]
Done when: If [X], then [Y]  ← negative/edge case
Done when: [NFR with exact threshold]

## Notes (optional)
[Design suggestion — framed as preference, not requirement]
[Links: mockup / SRD / related story ID]

## INVEST
[ ] I  [ ] N  [ ] V  [ ] E  [ ] S  [ ] T
```

---

## 10 · PRE-OUTPUT SELF-CHECK

Fix any failure before outputting.

- [ ] Actor is specific — not "user", "system", or "developer"
- [ ] Action is outcome-focused — no UI/technical prescriptions
- [ ] "so that" is present with genuine user/business value
- [ ] No `and` / `or` / `/` in WHO/DOES/WHAT
- [ ] Every AC has a clear pass/fail condition
- [ ] Happy path + at least one negative/edge case covered
- [ ] All AC completable within one sprint
- [ ] All 6 INVEST criteria pass
- [ ] NFRs use exact thresholds — no vague quantifiers
