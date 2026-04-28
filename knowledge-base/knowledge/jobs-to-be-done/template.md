# Jobs-to-be-Done Template

Use this template to capture a complete JTBD analysis. Fill in each section — skip categories only if they genuinely don't apply. The number of items per category should reflect what's real, not a fixed count.

## Provenance

Adapted from `prompts/jobs-to-be-done.md` in the `product-manager-prompts` repo. Expanded with elements from Ulwick's Outcome-Driven Innovation and Kalbach's JTBD Playbook.

---

## Template

```markdown
# Jobs-to-be-Done Analysis: [Product/Domain Name]

## 1. Job Performer

**Primary Job Performer:** [Who is executing the job? Be specific — role, not demographic]

**Other Roles in the Job Ecosystem:**
- Buyer: [Who makes the purchase decision?]
- Approver: [Who authorizes the acquisition?]
- Audience: [Who consumes the output of the job?]
- Other: [Any additional roles — manager, technician, assistant]

**Key distinction:** [How do the performer's needs differ from the buyer's?]

---

## 2. Main Job

**Core Functional Job:** [verb + object + clarifier — solution-agnostic, stable over time]

**Related Jobs** (adjacent objectives the performer has while doing the main job):
- [Related job 1]
- [Related job 2]
- [Add as many as relevant]

**Emotional Jobs** (how the performer wants to feel or avoid feeling):
- [Feel... / Avoid feeling...]
- [Feel... / Avoid feeling...]
- [Add as many as relevant]

**Social Jobs** (how the performer wants to be perceived, and by whom):
- [Be seen as... by...]
- [Be perceived as... by...]
- [Add as many as relevant]

---

## 3. Circumstances

**When and where does this job arise?**
- [Situational trigger 1 — e.g., "When facing a quarterly deadline"]
- [Situational trigger 2 — e.g., "While working remotely with a distributed team"]
- [Constraint 1 — e.g., "When budget for new tools is limited"]
- [Constraint 2 — e.g., "When onboarding to a new role"]
- [Add as many as relevant]

**Current solutions hired for this job:**
- [Solution 1 — include non-obvious alternatives like spreadsheets, workarounds, doing nothing]
- [Solution 2]
- [Why each solution gets "fired" or falls short]

---

## 4. Job Process Map

Map the main stages the performer goes through. Adapt these universal stages to fit the specific job:

| Stage    | What the performer is trying to do          | Key friction or gap     |
| -------- | ------------------------------------------- | ----------------------- |
| Define   | [Plan and set objectives for the job]       | [What goes wrong here?] |
| Locate   | [Gather needed inputs, info, or materials]  | [What goes wrong here?] |
| Prepare  | [Set up and organize before doing the work] | [What goes wrong here?] |
| Execute  | [Perform the core activity]                 | [What goes wrong here?] |
| Monitor  | [Check progress and quality]                | [What goes wrong here?] |
| Modify   | [Adjust when something changes]             | [What goes wrong here?] |
| Conclude | [Finish and wrap up]                        | [What goes wrong here?] |
| Share    | [Communicate results or hand off output]    | [What goes wrong here?] |

---

## 5. Needs — Approach A: Pains and Gains

Use this section for a lighter-weight analysis (workshops, early discovery, cross-functional collaboration).

### Pains

**Challenges** (obstacles preventing job completion):
- [Obstacle 1]
- [Obstacle 2]
- [Add as many as relevant]

**Costliness** (what takes too much time, money, or effort):
- [Cost 1 — be specific: "Manually updating X takes Y hours per week"]
- [Cost 2]

**Common Mistakes** (frequent errors that could be prevented):
- [Error 1]
- [Error 2]

**Unresolved Problems** (gaps in current solutions):
- [Gap 1]
- [Gap 2]

### Gains

**Expectations** (what would exceed current solutions):
- [Expectation 1]
- [Expectation 2]

**Savings** (time, money, or effort reductions that would delight):
- [Saving 1 — be specific: "Reduce X from Y hours to Z minutes"]
- [Saving 2]

**Adoption Factors** (what increases likelihood of switching):
- [Factor 1]
- [Factor 2]

**Life Improvement** (how a solution makes the performer's life better):
- [Improvement 1]
- [Improvement 2]

---

## 6. Needs — Approach B: Desired Outcome Statements (Optional, Higher Rigor)

Use this section when you need measurable, prioritizable needs for roadmap decisions or quantitative surveys.

**Format: direction of change + unit of measure + object of control + clarifier**

| Job Stage | Desired Outcome Statement                                     | Importance (1-10) | Satisfaction (1-10) | Opportunity Score |
| --------- | ------------------------------------------------------------- | ----------------- | ------------------- | ----------------- |
| [Stage]   | [Minimize/Maximize the time/likelihood/ability to... when...] |                   |                     |                   |
| [Stage]   | [Minimize/Maximize the time/likelihood/ability to... when...] |                   |                     |                   |
| [Stage]   | [Minimize/Maximize the time/likelihood/ability to... when...] |                   |                     |                   |

**Opportunity Score** = Importance + max(Importance − Satisfaction, 0)
Scores above 12 indicate significant unmet needs. Scores above 15 are critical opportunities.

---

## 7. Prioritization

### Pain Intensity Ranking
Rank your top pains from most to least intense. Consider: frequency, severity, and whether people have found workarounds.

1. [Most acute pain — explain why]
2. [Second most acute]
3. [Third most acute]

### Must-Have vs. Nice-to-Have Gains
- **Must-haves** (would drive someone to switch solutions): [list]
- **Nice-to-haves** (appreciated but wouldn't drive adoption alone): [list]

### Target Segments
Do different job performers have different unmet needs? If so, note the key differences:
- Segment A: [Who they are, what's uniquely unmet for them]
- Segment B: [Who they are, what's uniquely unmet for them]

---

## 8. Implications

**For product strategy:** [What should we build/improve based on the most critical unmet needs?]

**For messaging:** [How should we speak about our product in terms of the job, not features?]

**For competitive positioning:** [Where do current solutions fall short on the highest-opportunity outcomes?]

**What we still need to validate:** [Which assumptions need quantitative validation?]
```
