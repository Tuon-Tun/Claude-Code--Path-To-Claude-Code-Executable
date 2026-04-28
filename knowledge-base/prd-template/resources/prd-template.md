# [Product Name] - [Feature Name] PRD

---

## 1. Document Info

### 1.1 Version History

<!-- PM fills this section. Do not generate. -->

| Version | Last Updated | Modified By | Change Summary |
|---------|--------------|-------------|----------------|

### 1.2 References

<!-- PM fills this section. Do not generate. -->

| Document | Link | PIC |
|----------|------|-----|

---

## 2. Feature Overview

### 2.1 Problem Stateme   nt / Context

**Context**

- Current behavior:
- Existing gap:
- Business motivation:

**Problem Statement**

- **User problem:**
- **Business problem:**

---

### 2.2 Job to Be Done (JTBD)

<!--
  One block per distinct user type, role, or usage context - no upper limit.
  Think through every actor before deciding how many blocks to write.
-->

**JTBD - [User Type / Scenario]**

> When [situation], I want to [motivation], so I can [expected outcome].

| Dimension      | Description |
|----------------|-------------|
| Functional Job |             |
| Emotional Job  |             |
| Social Job     |             |

---

### 2.3 Goals & Success Metrics

**Goals:**

1.

**Success Metrics:**

| Metric | Baseline | Target |
|--------|----------|--------|

---

### 2.4 Assumptions & Open Questions

**Assumptions**

| ID | Assumption | Source / Confidence |
|----|------------|---------------------|

**Open Questions**

| ID | Question / Missing Information | Owner / Next Step |
|----|--------------------------------|-------------------|

---

## 3. Feature Specifications

### 3.1 Feature Epics & User Stories

<!--
  Structure all features using an Epic > User Story > Acceptance Criteria hierarchy.
  Follow the `user-story-skill` rules STRICTLY:
  - Epic groups related User Stories.
  - User Story format: As a [persona], I want to [action], so that [value/reason].
  - Acceptance Criteria: Format as `Done when: [positive/negative condition]`.

  Format example:
  **Epic 1: [Epic Name]**
  - **US-01 - [Story Name]**
    - **As a** [user role],
    - **I want to** [action],
    - **so that** [benefit].
    - **Acceptance Criteria**
      - Done when: [condition 1]
      - Done when: If [error], then [handling]
-->

### 3.2 Business Rules

<!--
  List every rule that constrains eligibility, pricing, permissions, limits, validation,
  sequencing, status transitions, timeout behavior, retry behavior, and exception handling.
  If the feature includes calculations, describe each calculation rule explicitly.
-->

- Rule 1:

### 3.3 Process Diagrams

<!-- Use the diagram-writer skill to generate diagrams for this feature.
     Available types: BPMN (bpmn.io XML), Activity Diagram (PlantUML), Sequence Diagram (PlantUML). -->

---

### 3.4 Use Case Specifications

<!--
  One UC block per User Story (UC-01 mirrors US-01, UC-02 mirrors US-02, and so on).

  For EACH UC, exhaustively enumerate before writing:

  ALTERNATIVE FLOWS - every valid deviation from the happy path:
    - User cancels or dismisses at any step
    - User chooses a different option or path
    - User skips an optional step
    - User modifies input before confirming
    - System triggers a retry or pagination
    -> Each distinct trigger = one row (A1, A2, A3, and so on). Do not stop at A1.

  EXCEPTION FLOWS - every error the system must handle:
    - Authentication failure or session expiry
    - Network timeout or service unavailable
    - Invalid or missing input
    - Server error (5xx)
    - Empty or no-result response
    - Rate limiting or quota exceeded
    - Concurrent modification conflict
    -> Each distinct error = one row (E1, E2, E3, and so on). Do not stop at E1.

  CRITICAL MANDATE: YOU MUST WRITE OUT ALL NECESSARY USE CASES FOR EVERY USER STORY.
  A SINGLE USER STORY MAY REQUIRE MULTIPLE USE CASES TO COVER ALL FUNCTIONALITIES.
-->

**UC-01 - [Use Case Name]**

| Field             | Detail |
|-------------------|--------|
| **Use Case ID**   |        |
| **Use Case Name** |        |
| **Actor**         |        |
| **Precondition**  |        |
| **Postcondition** |        |

**Main Flow (Happy Path):**

| Step | Actor | Action | System Response |
|------|-------|--------|-----------------|

**Alternative Flows:**

| Step | Trigger | Actor Action | System Response |
|------|---------|--------------|-----------------|

**Exception Flows:**

| Step | Error Condition | System Handling |
|------|-----------------|-----------------|

<!-- Repeat the full UC block above for UC-02, UC-03, and so on until coverage is complete. -->

---

### 3.5 Feature Requirements

#### Functional Requirements

<!--
  Derive from all User Stories and Acceptance Criteria. No fixed upper limit.
-->

| ID  | Requirement | Priority |
|-----|-------------|----------|

#### Non-Functional Requirements

| ID   | Requirement | Target |
|------|-------------|--------|

---

### 3.6 UI/UX Specifications

| Wireframe / UI Element | Description | Validation / Rule |
|------------------------|-------------|-------------------|

---

### 3.7 API / Technical Specs

| Endpoint | Method | Request Payload | Response | Error Handling |
|----------|--------|-----------------|----------|----------------|

---

*Document generated using the PRD template renderer.*
