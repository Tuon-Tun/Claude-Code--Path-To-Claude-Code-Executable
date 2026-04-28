# Jobs-to-be-Done Examples

## Example 1: Project Management Software (Full JTBD Analysis)

### 1. Job Performer

**Primary Job Performer:** Project lead managing a cross-functional product development team (5–15 people)

**Other Roles:**

- Buyer: VP of Engineering or IT procurement (evaluates cost, security, integration)
- Approver: CFO or department budget holder
- Audience: Stakeholders and executives who receive status updates
- Assistant: Scrum master or project coordinator who maintains the tool day-to-day

**Key distinction:** The project lead cares about visibility and control. The buyer cares about cost per seat, SSO compliance, and whether it replaces existing tools. These are different needs.

### 2. Main Job

**Core Functional Job:** Coordinate work across a cross-functional team to deliver a project on time

**Related Jobs:**

- Report project status to stakeholders
- Manage resource allocation across concurrent projects
- Onboard new team members mid-project

**Emotional Jobs:**

- Feel confident that nothing is slipping through the cracks
- Avoid the stress of last-minute surprises when a deadline approaches
- Feel a sense of progress and momentum, not just firefighting

**Social Jobs:**

- Be seen as an organized, reliable project leader by the executive team
- Demonstrate transparency and accountability to stakeholders
- Appear competent and in-control to direct reports

### 3. Circumstances

- When the team is distributed across time zones (no hallway conversations)
- When multiple workstreams have dependencies on each other
- During crunch periods when priorities shift rapidly
- When onboarding a contractor or new hire who needs context quickly
- When switching from a previous tool (Jira, Asana, spreadsheets) mid-project

**Current solutions hired:**

- Jira: powerful but complex; non-engineers resist using it; configuration overhead is high
- Spreadsheets: flexible but no real-time sync; becomes stale within hours
- Slack threads + memory: fast but nothing is documented; context is lost when people join
- Weekly status meetings: reliable but expensive (5+ hours/week across the team)

### 4. Job Process Map

| Stage    | What the performer does                                                    | Key friction                                                                    |
| -------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Define   | Set project goals, scope, and success criteria                             | Hard to translate business objectives into concrete deliverables and milestones |
| Locate   | Identify who's available, what skills are needed, what's already been done | No single view of team capacity across projects                                 |
| Prepare  | Break work into tasks, assign owners, set timelines                        | Estimating effort is guesswork without historical data                          |
| Execute  | Team members work on assigned tasks                                        | Different people update status in different tools (or not at all)               |
| Monitor  | Track progress against deadlines, identify blockers                        | Blockers surface too late — often at standup, not when they happen              |
| Modify   | Re-prioritize when scope changes or a dependency breaks                    | Cascading impact of changes is invisible until it's too late                    |
| Conclude | Deliver the project, conduct retrospective                                 | Lessons learned aren't captured in a way that's reusable                        |
| Share    | Report status to stakeholders, hand off to next phase                      | Manually assembling status reports takes hours and is always slightly outdated  |

### 5. Needs — Pains and Gains

**Pains — Challenges:**

- Team members use different tools (Slack, email, spreadsheets), creating information silos
- No single source of truth for project status — everyone has a slightly different picture
- Dependencies between workstreams are invisible until something breaks
- Remote team members miss context shared in impromptu conversations

**Pains — Costliness:**

- Manually updating status reports takes 3 hours per week
- Sync meetings to align everyone consume 5+ hours per week across the team
- Onboarding a new team member takes 2+ days of someone's time to provide context

**Pains — Common Mistakes:**

- Forgetting to follow up on tasks without clear ownership or due dates
- Miscommunicating priority changes, leading to wasted effort on deprioritized work
- Overcommitting a team member who's already allocated to other projects

**Pains — Unresolved Problems:**

- Current tools don't surface blockers automatically — they require people to self-report
- Hard to visualize dependencies and cascading impact of timeline changes
- No way to see historical velocity to improve future estimates

**Gains — Expectations:**

- Automatically updates stakeholders on progress without manual report assembly
- Suggests task owners based on workload, skills, and availability
- Alerts the project lead to at-risk items before they become blockers

**Gains — Savings:**

- Reduce status reporting time from 3 hours to 15 minutes per week
- Cut sync meetings from 5 hours to 2 hours per week
- Reduce new team member onboarding from 2 days to 2 hours

**Gains — Adoption Factors:**

- Easy to onboard (< 30 minutes to set up for the team)
- Integrates with tools already in use (Slack, Google Calendar, GitHub)
- Doesn't require the whole team to change habits on day one — works with partial adoption

**Gains — Life Improvement:**

- Leave work on time instead of staying late to track down updates
- Feel proactive about project health instead of constantly reactive
- Spend time on strategic decisions instead of administrative overhead

### 6. Desired Outcome Statements (Selected High-Priority)

| Job Stage | Desired Outcome                                                               | Imp | Sat | Opp |
| --------- | ----------------------------------------------------------------------------- | --- | --- | --- |
| Monitor   | Minimize the time it takes to identify a blocked task                         | 9   | 3   | 15  |
| Modify    | Minimize the likelihood of missing a cascading impact when a deadline changes | 9   | 2   | 16  |
| Share     | Minimize the time it takes to assemble an accurate status report              | 8   | 3   | 13  |
| Execute   | Minimize the likelihood that two team members unknowingly duplicate work      | 7   | 4   | 10  |
| Prepare   | Increase the accuracy of effort estimates for new tasks                       | 8   | 3   | 13  |
| Locate    | Minimize the time it takes to determine a team member's current availability  | 7   | 3   | 11  |

### 7. Why This Works

- **Jobs are specific and solution-agnostic.** "Coordinate work across a cross-functional team" — not "use a project management tool."
- **The performer is distinguished from the buyer.** Their needs are different and both matter.
- **Circumstances give context.** "Distributed team" and "mid-project tool switch" create design constraints.
- **The job map reveals where friction lives.** It's not just "project management is hard" — it's specifically the Monitor and Modify stages where the worst breakdowns happen.
- **Pains are validated with specifics.** "3 hours per week" is actionable. "Tools are bad" is not.
- **Gains are measurable.** "Reduce from 3 hours to 15 minutes" can be verified.
- **Desired outcomes are prioritizable.** Opportunity scores point to the highest-value problems to solve.

---

## Example 2: Bad JTBD Analysis (Feature Wishlist)

**Job Performer:** Not specified

**Main Job:** "Use AI-powered project management"

**Emotional Jobs:** "Feel modern"

**Social Jobs:** "Be seen as innovative"

**Pains:**

- Current tools are old
- UX is bad
- Need more automation

**Gains:**

- Better dashboards
- AI features
- Mobile app
- Faster performance

### Why This Fails

**No job performer defined.** Who are we solving for? A project lead? A team member? An executive? Each has different jobs and needs.

**The "job" is actually a solution.** "Use AI-powered project management" bakes in the technology. What are they trying to *accomplish* with AI? If you strip out "AI-powered," the job might be "identify project risks before they cause delays" — that's a real job that could be solved many ways.

**"Have dashboards" and "Mobile app" are features, not jobs.** What would the dashboard help them *do*? What would they do on mobile that they can't do now? Dig deeper.

**Pains are vague.** "Current tools are old" — old how? What specifically can't they do? "UX is bad" — every stakeholder in every company says this. It's not actionable.

**Gains are generic.** "Better UX" and "faster performance" are things every product promises. They tell you nothing about what's uniquely unmet for your customers.

**No circumstances.** When does this matter most? For whom? Under what conditions?

**No process map.** Where in the workflow do things actually break down? Without this, you're guessing at solutions.

### How to Fix It

1. **Define the job performer.** Interview 8–12 people who actually do the job. Not their managers. Not your sales team's interpretation.
2. **Reframe from solutions to jobs.** Ask "What are you trying to accomplish?" not "What features do you want?" Use the "5 Whys" technique: "I need AI" → Why? → "To predict risks" → Why? → "To avoid missed deadlines" → The job is "deliver projects on time."
3. **Map the process.** Walk through a recent project step by step. Where did things go wrong? Where did they spend the most time? Where did they feel most frustrated?
4. **Get specific on pains.** Replace "UX is bad" with "It takes 6 clicks and 3 screen changes to reassign a task, which means people don't do it and tasks go stale."
5. **Make gains measurable.** Replace "better dashboards" with "See the status of all active workstreams in under 10 seconds without opening multiple views."

---

## Example 3: B2C Quick Analysis — Home Cooking App

### Job Performer

Home cook who prepares weeknight dinners for a family of 3–5 people.

### Main Job

Prepare a healthy weeknight dinner that the family will eat.

### Related Jobs

- Plan meals for the week
- Shop for groceries efficiently
- Use up ingredients before they expire

### Emotional Jobs

- Feel like a good parent who provides nutritious meals
- Avoid the guilt of ordering takeout again
- Feel creative and not stuck in a recipe rut

### Social Jobs

- Have family members compliment the meal
- Be seen by partner as sharing the domestic workload

### Circumstances

- After a full workday, with 30–45 minutes available for cooking
- When one family member has dietary restrictions (e.g., a picky child, an allergy)
- When the fridge is half-empty and grocery shopping isn't happening today

### Key Pains

- Meal planning takes mental energy the cook doesn't have after work
- Recipes online assume ingredients the cook doesn't have on hand
- Following a recipe with kids needing attention means constant interruptions — steps need to be glanceable, not paragraph-length

### Key Gains

- Suggests meals based on what's already in the fridge
- Adapts portions automatically for different family sizes
- Provides 15-minute and 30-minute options for different energy levels

### Why This Works at a Lighter Depth

Not every analysis needs 150 desired outcome statements. For a consumer app in early discovery, this level of specificity is enough to start designing and testing. The key elements are present: a defined performer, a clear functional job, emotional/social dimensions, circumstances that constrain the solution, and specific pains grounded in real behavior. You can deepen with desired outcomes later when prioritizing the roadmap.
