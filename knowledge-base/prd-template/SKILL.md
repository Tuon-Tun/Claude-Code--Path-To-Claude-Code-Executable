---
name: prd-template-renderer
description: >
  Render a full PRD from an approved structured brief and domain context. Use when the
  orchestrator has already collected and approved the feature JSON and needs the standard PRD
  filled end-to-end without re-interviewing the user.
---

# PRD Template Renderer

Produce a complete PRD from an approved structured brief, then fill `resources/prd-template.md`.
Scope: PRD drafting only. Review and export are separate steps in the pipeline.

---

## Phase 1 - Inputs

Before drafting, confirm you have:

1. The approved JSON brief from Step 1
2. The approved Product Framing Pack from Step 2, including JTBD statements, Epics, User Stories, Acceptance Criteria, and open questions
3. Domain context from `domain-knowledge/[Domain_Name]/rules.md` when running in `IDE_FULL_PIPELINE`
4. Relevant domain history from prior PRDs or inputs, if present
5. Standards from:
   - `knowledge-base/knowledge/jobs-to-be-done/SKILL.md`
   - `knowledge-base/knowledge/user-story-skill/SKILL.md`

Do not re-interview the user if the orchestrator already completed the JSON and Product Framing approval steps. Only stop and request clarification if a critical field remains blocked after Step 2 approval.
If JTBD research is not provided in the approved brief, Product Framing Pack, or domain context, label JTBD outputs as hypothesized and needing validation.

---

## Phase 2 - Draft

Load `resources/prd-template.md`. Fill every section. Use `TBD` only when the approved brief still contains an unresolved gap.

**Rules:**

- Acceptance Criteria must follow the `Done when` standard from `user-story-skill`.
- Apply JTBD and user-story standards strictly; do not shortcut them to save tokens.
- Use the approved Product Framing Pack as the source of truth for Section 2.2 and Section 3.1.
- If `Epic_Candidates` or `User_Story_Candidates` are present in the brief, use them only as seeds already resolved by the approved Product Framing Pack.
- Surface `Assumptions`, `Missing_Information`, and unresolved `[NEEDS_CLARIFICATION]` items in Section 2.4 Assumptions & Open Questions.
- Functional Requirements must include a `High / Medium / Low` priority.
- API details not provided -> mark `[DEV TO COMPLETE]`.
- Use Case tables must include Actor, Precondition, Postcondition, Main Flow, Alternative Flow, and Exception Flow.
- Section 3.3 must include only the diagram types explicitly approved by the user.
- Preserve the selected `Delivery_Mode`; drafting does not decide whether to save files or export DOCX.

---

## Phase 3 - Section 3.3 Diagrams

**Critical rule:** Only generate diagrams for the types explicitly approved by the user in Step 0 or Step 1. Do not substitute plain text or Mermaid when BPMN, Activity Diagram, or Sequence Diagram is requested.

When Section 3.3 needs one or more diagrams, **delegate entirely to `knowledge-base/prd-template/diagram-writer/SKILL.md`** using its Input Contract. Do not generate diagram code inline here.

Pass to `diagram-writer`:
- The diagram type(s) from `Diagram_Requirements` in the approved JSON
- The feature name and description
- The actors and system components involved
- The happy path steps from `User_Flow`
- Key edge cases and error scenarios from `Business_Logic_and_Rules`

After `diagram-writer` returns the output, embed it verbatim in Section 3.3 of the PRD.

---

## Phase 4 - Versioning

Do not pre-fill Version History by default; the PM owns it. Keep the table format empty unless the workflow explicitly requests a starting row. If a starting row is explicitly requested, use `0.1`, today's date, `PRD pipeline`, and `Initial draft`.

---

## Quality Checklist

- All template section headers are present.
- Section 3.3 contains only the diagrams explicitly requested by the user.
- No blank sections remain; use `TBD` when information is still pending.
- The language matches the user's language.
