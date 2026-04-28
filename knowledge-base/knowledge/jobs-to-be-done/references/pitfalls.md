# Common Pitfalls and Troubleshooting

These are the mistakes practitioners make most frequently when applying JTBD. Each pitfall includes symptoms, consequences, and a concrete fix.

---

## Pitfall 1: Confusing Jobs with Solutions

**Symptom:** Job statements contain technology, product names, or features — "Use Slack to communicate," "Build a dashboard," "Implement AI-powered analytics."

**Consequence:** You've anchored on a delivery mechanism, not the underlying objective. This closes off alternative solutions and makes the analysis obsolete when technology changes.

**Fix:** Apply the "5 Whys" technique:
- "I need Slack" → Why? → "To communicate with my team" → Why? → "To get quick answers to unblock my work" → Why? → "To avoid project delays caused by waiting for information."
- The job is "get timely answers to unblock work." Slack is one possible solution. So is better documentation, office hours, or async video.

**Quick test:** Would this job statement have made sense 20 years ago? If not, you probably have a solution embedded in it.

---

## Pitfall 2: Generic, Unfocused Jobs

**Symptom:** Jobs are broad platitudes — "Be more productive," "Save time," "Improve efficiency," "Grow the business."

**Consequence:** Too vague to inform product decisions. Every product in the world claims to help people "be more productive." There's no way to differentiate or prioritize.

**Fix:** Get specific by asking "How?" to move down a level:
- "Save time" → How? → "Reduce the time spent generating monthly reports" → How? → "Automatically pull data from three systems into a single report format."
- The job is "generate monthly performance reports." The need is "minimize the time it takes to consolidate data from multiple sources."

**Rule of thumb:** If a job could apply to any industry and any product, it's too broad.

---

## Pitfall 3: Ignoring Emotional and Social Jobs

**Symptom:** The analysis only documents functional tasks. No mention of how people feel or how they want to be perceived.

**Consequence:** You miss the motivators that often drive purchasing decisions. People frequently choose solutions based on emotional and social factors even when a functionally superior alternative exists. (Think Apple vs. competitors — functional parity, emotional and social differentiation.)

**Fix:** In interviews, explicitly ask:
- "How would it feel if this job got significantly easier?"
- "Who notices when this job goes well? When it goes badly?"
- "How do you want your [boss/client/team/family] to see you in relation to this?"

Don't fabricate emotional jobs from assumptions. They should come from research.

**Important nuance:** Solve the functional job first, then layer emotional and social dimensions. If the functional job isn't done, emotional satisfaction won't follow. But once functional parity is achieved among solutions, emotional and social jobs become the primary differentiators.

---

## Pitfall 4: Fabricating JTBD Without Research

**Symptom:** The template is filled out entirely from internal assumptions. No customer interviews, no observation, no data.

**Consequence:** You're guessing. JTBD analysis is only valuable when grounded in what real people actually experience. Internal teams systematically overestimate the importance of their own product and underestimate customers' workarounds.

**Fix:** Talk to 8–12 people who perform the job. At minimum, use one of these approaches:
- **Switch interviews** — talk to people who recently switched to or from a solution. What triggered the switch? What were they hiring the new solution to do?
- **Contextual inquiry** — observe people performing the job in their actual environment. What's on their screen? What's on their desk? Where do they get stuck?
- **Outcome-driven interviews** — walk through the job process step by step and ask, at each stage, "How do you measure success here? What goes wrong?"

See `references/research-methods.md` for detailed guidance.

If research hasn't been done, say so explicitly in the analysis. Label assumptions as assumptions. This is far better than presenting guesses as validated insights.

---

## Pitfall 5: Treating All Pains as Equal

**Symptom:** The analysis lists 15–20 pains with no ranking, grouping, or prioritization.

**Consequence:** No clarity on what to solve first. Product teams try to address everything or pick based on what's easiest to build rather than what matters most to customers.

**Fix:** Rank pains on two dimensions:
1. **Intensity:** How painful is this? (Acute and blocking vs. mild annoyance)
2. **Frequency:** How often does this happen? (Daily vs. once a year)

The intersection of high intensity and high frequency is where the biggest opportunities live.

For more precision, use the Opportunity Algorithm from Ulwick's ODI: for each desired outcome, rate importance (1–10) and satisfaction (1–10), then calculate Opportunity = Importance + max(Importance − Satisfaction, 0). Focus on outcomes scoring above 12.

Ask the forcing question: "If we could only solve one pain, which would have the biggest impact on whether someone would switch to our solution?"

---

## Pitfall 6: No Job Performer Defined

**Symptom:** The analysis talks about "users" or "customers" without specifying who the job performer is. Or it conflates the end user with the buyer.

**Consequence:** Different people in the job ecosystem have different needs. If you design for the buyer's needs (cost, compliance, procurement ease) but neglect the performer's needs (daily usability, workflow fit), you get "shelfware" — products that are purchased but not used.

**Fix:** Name the job performer by role and context, not by demographic. "35-year-old male, college-educated" tells you nothing about jobs. "Project lead managing a distributed team of 8–12 engineers" tells you everything.

Then explicitly map other roles: Who buys? Who approves? Who consumes the output? Whose needs might conflict with the performer's?

---

## Pitfall 7: Missing Circumstances

**Symptom:** Jobs are stated in a vacuum — "prepare a meal," "file taxes," "manage a project" — without any context about when, where, or under what conditions.

**Consequence:** The analysis is too abstract to drive specific design decisions. A meal prepared on a relaxed Sunday afternoon is a completely different design challenge than a meal prepared after work in 25 minutes for picky children.

**Fix:** For every main job, identify at least 3–5 circumstances that shape how it gets done. Focus on:
- Time constraints
- Environmental factors
- Resource limitations
- Emotional state of the performer
- Who else is involved or affected

Circumstances are what make a generic job into an actionable innovation target.

---

## Pitfall 8: Wrong Level of Abstraction

**Symptom:** The job is either so broad it's an aspiration ("live a fulfilling life") or so narrow it's a UI task ("click the submit button").

**Consequence:** Too broad = endless possibilities, no focus. Too narrow = you're designing a button, not solving a problem.

**Fix:** Use the hierarchy:
- **Aspiration**: "Be financially secure" — useful for messaging, not for scoping a product
- **Big Job**: "Plan long-term retirement savings" — good scope for a product or product line
- **Little Job**: "Evaluate investment fund performance" — good scope for a feature set
- **Micro-Job**: "Compare two fund fact sheets side by side" — good scope for a UX interaction

Match the level to your goal. Strategy discussions should operate at the Big Job level. Feature design should operate at Little Job or Micro-Job level.

---

## Troubleshooting: When the Analysis Doesn't Feel Right

**"Everything looks correct but it's not useful."**
The analysis probably lacks specificity. Check: Are pains stated with concrete details (numbers, frequencies, consequences)? Are the circumstances specific enough to constrain the solution space? If you could hand this to a designer and they'd know where to start, it's specific enough.

**"We have too many jobs and can't focus."**
You're probably operating at too fine a level of granularity. Zoom out. Group related micro-jobs under a single big job. Then decide which big job to focus on based on strategic fit and unmet need intensity.

**"Stakeholders don't agree on the main job."**
This is actually valuable information — it means you haven't aligned on who the customer is. Go back to Job Performer. Once you agree on *who* you're solving for, the main job usually becomes clearer.

**"The customer says they want features, not jobs."**
That's normal. Customers articulate solutions because that's what they know. Your job is to translate. For every feature request, ask "What would that help you accomplish?" three times. You'll get to the job.

**"We don't have time/budget for customer research."**
Start with what you have. Internal teams who interact with customers daily — support, sales, customer success — carry significant tacit knowledge. Run a 60-minute workshop where each person shares the top 3 frustrations they hear from customers. This isn't a substitute for primary research, but it's better than pure assumption. Label the output as "hypothesized JTBD — needs validation."
