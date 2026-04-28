# Bad User Story Examples — Analysis & Fixes

---

## Bad Example 1 — Missing Structure Entirely

**Bad:**

```text
I can filter shoes by size.
```

**What's wrong:**

- No actor — no user perspective
- No "so that" — no value or reason
- Statement of capability, not user outcome
- No basis for writing AC

**Fixed Story:**

```text
As a Shopper,
I want to filter products by shoe size,
so that I can quickly find items available in my size without browsing irrelevant results.
```

**Fixed AC:**

```text
Done when: The shopper can select one or more shoe sizes from a filter panel on the product listing page.
Done when: The product list updates to show only items available in the selected size(s).
Done when: If no products match the selected size filter, the page displays "No results found for this size."
Done when: The shopper can clear all size filters to return to the full product listing.
```

---

## Bad Example 2 — Prescribing a UI Solution

**Bad:**

```text
As a food service customer,
I want food item types to be displayed in groups,
so that I can locate them more quickly on the screen.
```

**What's wrong:**

- "Displayed in groups" prescribes a specific UI design — limits team creativity
- Real user need is **findability**, not visual grouping
- Locks the team into one solution before exploring better options

**Fixed Story:**

```text
As a Food Service Customer,
I want to easily locate specific food item types on the ordering screen,
so that I can build my order efficiently without searching through irrelevant items.
```

**Fixed AC:**

```text
Done when: The customer can locate any food item type within 3 interactions from the order screen.
Done when: The ordering interface provides a way to browse or filter food items by category.
Done when: The customer can search for a food item by name and see matching results within 1 second.
Done when: If a food item type has no available items, it is either hidden or labelled as "Unavailable."
```

---

## Bad Example 3 — Developer as the Actor

**Bad:**

```text
As a developer,
I want to reorganise this code to make it easier and faster to code in this module in the future.
```

**What's wrong:**

- "Developer" is not an end user of the product
- The benefit is to the developer, not the business or end user
- This is a technical refactoring task — not a User Story
- No user value can be traced from this statement

**Fixed approach — reframe as a Technical Task with a value link:**

```text
Technical Task: Refactor [module name] to reduce code complexity.
Reason: Enables faster delivery of future features in this area, reducing time-to-market for [feature set].
```

**If a user-facing story genuinely exists behind this work, write it properly:**

```text
As a [end user who benefits from faster feature delivery],
I want to [the user-facing outcome the refactor enables],
so that [the business or user value].
```

**Fixed AC (for the user-facing story):**

```text
Done when: [User-facing feature enabled by the refactor works as expected]
Done when: [Performance or reliability improvement is measurable and verified]
Done when: [Regression — existing functionality is not broken by the refactor]
```

---

## Bad Example 4 — Prescribing a Technical Solution

**Bad:**

```text
As a user,
I want a dropdown with autocomplete and API-based search functionality,
so that I can quickly find products.
```

**What's wrong:**

- Prescribes implementation (dropdown, autocomplete, API-based search) — removes team creativity
- Actor "user" is too generic — no persona or context
- Real goal is **finding products quickly**, not using a specific UI control

**Fixed Story:**

```text
As a Shopper,
I want to find products quickly and easily from any page,
so that I can save time and complete my shopping without frustration.
```

**Fixed AC:**

```text
Done when: The shopper can search for a product by name and see relevant results within 1 second.
Done when: Search results update as the shopper types (minimum 3 characters entered).
Done when: If the search returns no results, a message displays: "No products found. Try a different search term."
Done when: The search is accessible from the navigation bar on all pages of the site.
Done when: Search works correctly on mobile devices with touch input.
```

---

## Bad Example 5 — Vague NFR

**Bad AC:**

```text
Done when: The website accepts more than 3,000 users to connect simultaneously.
```

**What's wrong:**

- "More than 3,000" is vague — 20,000 also satisfies this but is a completely different requirement
- No performance outcome defined — what happens at the threshold?
- Cannot be tested precisely

**Fixed AC:**

```text
Done when: The website supports up to 5,000 concurrent user connections without response times exceeding 3 seconds.
Done when: When concurrent users exceed 5,000, the system queues additional requests and displays "High traffic — please wait" rather than an error.
Done when: Load testing confirms these thresholds under simulated conditions before release.
```

---

## Bad Example 6 — "Need" Trap

**Bad:**

```text
As a Customer,
I need a button that submits my payment.
```

**What's wrong:**

- "Need" leads to a design requirement (a button) rather than a user outcome
- Describes a UI element, not an action or goal
- Team has no idea WHY payment is being submitted or what success looks like

**Fixed Story:**

```text
As a Customer,
I want to complete and submit my payment securely,
so that I can finalise my purchase and receive confirmation that my order has been placed.
```

**Fixed AC:**

```text
Done when: The customer can enter payment details (card number, expiry, CVV) on the checkout screen.
Done when: The customer can submit their payment and receive an on-screen confirmation within 5 seconds.
Done when: The customer receives a confirmation email within 2 minutes of successful payment.
Done when: If payment is declined, the customer sees a clear error message and can retry or use a different payment method.
Done when: All payment data is transmitted over HTTPS and no card details are stored in plain text.
```

---

## Bad Example 7 — Multiple Actors in One Story

**Bad:**

```text
As a Customer Service Rep, Admin, and Supervisor,
I want to update customer demographic data.
```

**What's wrong:**

- Multiple actors crammed into one subject — cannot always be built and tested together
- Makes AC impossible to write clearly per role
- Violates single actor, single action, single outcome rule

**Fixed — One story with role-based AC (if all roles share the same build + test path):**

```text
As a CSR System User,
I want to update customer demographic data,
so that customer records remain accurate.
```

```text
Done when: A Customer Service Rep can update demographic data.
Done when: An Admin can update demographic data.
Done when: A Supervisor can update demographic data.
Done when: Each update is logged with the user's role and timestamp.
```

**Or — split into separate stories (if roles require different build or test paths):**

```text
US-101: As a Customer Service Rep, I want to update demographic data...
US-102: As an Admin, I want to update demographic data...
US-103: As a Supervisor, I want to update and audit demographic data...
```
