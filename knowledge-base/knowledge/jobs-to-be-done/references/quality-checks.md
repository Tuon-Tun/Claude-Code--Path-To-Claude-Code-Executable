# Quality Checks and Formulation Rules

Use this reference to validate job statements, need statements, and the overall JTBD analysis. These rules are drawn from Ulwick's ODI methodology and Kalbach's JTBD Playbook.

---

## Job Statement Rules

A well-formed job statement follows: **verb + object + clarifier**

### Dos

| Rule                                 | Example                                                   |
| ------------------------------------ | --------------------------------------------------------- |
| Reflect the individual's perspective | "Reconcile monthly business expenses"                     |
| Start with a verb                    | "Coordinate tasks across a distributed team"              |
| Ensure stability over time           | "Listen to music while exercising" (same job for decades) |
| Clarify with context if needed       | "File annual taxes for a small business"                  |
| Have a clear "done" state            | "Prepare a meal for dinner" (done when meal is ready)     |

### Don'ts

| Rule                                  | Bad Example                                       | Fix                                                     |
| ------------------------------------- | ------------------------------------------------- | ------------------------------------------------------- |
| Never include solutions or technology | "Use Slack to communicate with the team"          | "Communicate with remote teammates"                     |
| No methods or techniques              | "Search by keyword for documents in the database" | "Retrieve relevant content"                             |
| No adjectives (those are needs)       | "Quickly find cheap airfares"                     | "Find airfares" — quick and cheap are needs             |
| No compound concepts (no AND/OR)      | "Plan and book a vacation"                        | Split: "Plan a vacation" and "Book travel arrangements" |
| No observations or preferences        | "People prefer nearby conferences"                | "Attend professional events"                            |
| Don't start with "Help me..."         | "Help me organize my files"                       | "Organize digital files"                                |
| Avoid vague verbs                     | "Manage finances"                                 | "Track business expenses for tax deductions"            |

### Level Check

If a job statement feels too broad, ask "How?" to move down a level.
If it feels too narrow, ask "Why?" to move up.

| Too Broad                               | Right Level                              | Too Narrow                               |
| --------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| "Be financially secure" (aspiration)    | "Plan long-term retirement savings"      | "Enter a number into a spreadsheet cell" |
| "Be a better professional" (aspiration) | "Develop expertise in a new domain"      | "Click the 'enroll' button"              |
| "Stay healthy" (aspiration)             | "Maintain a consistent exercise routine" | "Tie running shoes"                      |

---

## Desired Outcome Statement Rules

A well-formed desired outcome follows: **direction of change + unit of measure + object of control + clarifier**

### Direction of Change (always starts with one of these)

- **Minimize** / Decrease / Reduce — for things the performer wants less of
- **Maximize** / Increase / Raise — for things the performer wants more of

### Common Units of Measure

- Time ("the time it takes to...")
- Likelihood ("the likelihood of..." or "the likelihood that...")
- Ability ("the ability to...")
- Number ("the number of...")
- Frequency ("the frequency with which...")
- Effort ("the effort needed to...")

### Validation Checklist for Outcome Statements

Each desired outcome statement should pass ALL of these checks:

- [ ] **Starts with a direction word** (minimize, maximize, increase, reduce)
- [ ] **Contains a measurable unit** (time, likelihood, ability, number, effort)
- [ ] **Is solution-agnostic** — no mention of specific tools, features, or technologies
- [ ] **Is controllable** — the product team could actually influence this metric
- [ ] **Is stable over time** — this outcome would be desired regardless of the current solution
- [ ] **Is atomic** — contains only one concept (no ANDs or ORs)
- [ ] **Has a clarifier** — provides enough context to be unambiguous

### Examples: Good vs. Bad

| Bad                               | Issue                   | Good                                                                                               |
| --------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------- |
| "Make reports faster"             | Vague, no structure     | "Minimize the time it takes to generate an accurate status report"                                 |
| "Better collaboration"            | Not measurable          | "Increase the likelihood that all team members have current project context"                       |
| "Use AI to predict risks"         | Contains a solution     | "Minimize the likelihood of discovering a project risk after it causes a delay"                    |
| "Reduce cost and improve quality" | Compound (two concepts) | Split into two: "Reduce the cost per unit produced" and "Minimize the number of defects per batch" |
| "Minimize time"                   | No object or clarifier  | "Minimize the time it takes to onboard a new team member to full productivity"                     |

---

## Pains/Gains Validation

### Pain Statement Quality Checks

- [ ] **Specific, not vague:** "Tools are bad" → fails. "Team members update status in 3 different tools, so there's no single source of truth" → passes.
- [ ] **Grounded in behavior, not opinion:** Describes what actually happens, not what someone thinks in the abstract.
- [ ] **Includes a consequence:** Why does this pain matter? "Manual reports take 3 hours/week" is better than just "manual reports" — the time cost is the pain.
- [ ] **Not a disguised solution:** "We need a dashboard" is a solution. "We can't see cross-project status without opening 4 different tools" is a pain.

### Gain Statement Quality Checks

- [ ] **Measurable or observable:** "Better UX" → fails. "Complete the most common task in under 3 clicks" → passes.
- [ ] **Tied to the job, not to a feature:** "Has AI" → fails. "Identifies at-risk items before they cause delays" → passes.
- [ ] **Differentiated:** Would this gain distinguish one solution from another? If every product claims it, it's not useful.

---

## Overall Analysis Quality Checks

After completing the full JTBD analysis, verify:

- [ ] **Job performer is defined** and distinguished from the buyer
- [ ] **Main job is functional** and follows verb + object + clarifier
- [ ] **Emotional and social jobs are separate** from functional jobs
- [ ] **Circumstances are captured** — the job has context, not just an abstract statement
- [ ] **Current solutions are documented** — including non-obvious alternatives and workarounds
- [ ] **Pains come from research**, not assumptions — if no research has been done, flag this explicitly
- [ ] **Gains are specific enough to test** — a product team could verify whether the gain is achieved
- [ ] **The analysis doesn't confuse jobs with solutions** — scan every statement for embedded technology or feature references
- [ ] **Needs are prioritized** — not just listed. Intensity matters.
- [ ] **Different segments are considered** — do all performers have the same unmet needs, or are there distinct groups?
