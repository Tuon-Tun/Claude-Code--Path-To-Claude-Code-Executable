# Good User Story Examples

---

## Example 1 — Claims & Permissions (Financial Services)

**Story:**

```text
As a Claims Supervisor,
I want to access payment permissions,
so that I can know which reps on my team are authorised to make digital payments.
```

**Why it works:**

- Actor is specific (Claims Supervisor — not "user" or "manager")
- Action is outcome-focused — gaining knowledge, not clicking a screen
- Value is clear — oversight and control of authorised digital payments

**Acceptance Criteria:**

```text
Done when: The Claims Supervisor can view a list of all reps on their team.
Done when: The list indicates which reps are authorised to make digital payments.
Done when: The list indicates which reps are not authorised to make digital payments.
Done when: A Customer Service Rep cannot access the payment permissions screen.
Done when: The permissions list reflects real-time data, not cached results older than 5 minutes.
```

---

## Example 2 — Project Management Visibility

**Story:**

```text
As a Project Manager,
I want to view team workload,
so that I can assign tasks more effectively and prevent team burnout.
```

**Why it works:**

- Actor is specific and relatable
- Action is outcome-focused — viewing workload, not "seeing a dashboard"
- Value covers both the manager's goal and the broader team benefit

**Acceptance Criteria:**

```text
Done when: The project manager can see a workload view showing all active tasks per team member.
Done when: Tasks are displayed with estimated effort and due date.
Done when: The view highlights team members exceeding 100% capacity in a visually distinct way.
Done when: The workload view updates in real time as tasks are assigned or completed.
Done when: If no tasks are assigned to a team member, the view shows 0% utilisation.
```

---

## Example 3 — Order Notifications (E-commerce)

**Story:**

```text
As a Customer,
I want to receive order notifications,
so that I stay updated on my delivery status without having to check manually.
```

**Why it works:**

- Actor is the direct end user
- Action focuses on the user's goal — staying informed, not the delivery mechanism
- Value solves a real frustration — not knowing where your order is

**Acceptance Criteria:**

```text
Done when: The customer receives a notification when their order is confirmed.
Done when: The customer receives a notification when their order is shipped.
Done when: The customer receives a notification when their order is out for delivery.
Done when: The customer receives a notification when their order is delivered.
Done when: If the customer has opted out of notifications, they receive no automated messages.
Done when: Notifications are sent within 5 minutes of the relevant status change. (Customer's preference is email.)
```

---

## Example 4 — Admin Password Reset (IT / Support)

**Story:**

```text
As an Admin,
I want to reset user passwords,
so that I can help users regain account access quickly and reduce support wait times.
```

**Why it works:**

- Actor is specific with a clear support role
- Action is outcome-focused — resetting passwords, not "clicking a button"
- Value ties to both the user's need (regain access) and the business benefit (reduce support time)

**Acceptance Criteria:**

```text
Done when: The admin can search for a user by name or email address.
Done when: The admin can trigger a password reset for any found user account.
Done when: The user receives a password reset email within 2 minutes of the admin triggering the reset.
Done when: The reset link expires after 24 hours.
Done when: If the user account is locked, the admin can unlock it alongside the password reset.
Done when: If the admin searches for a non-existent account, the system displays "No account found" and does not error.
Done when: All password reset actions are logged with the admin's ID and timestamp for audit purposes.
```

---

## Example 5 — Wishlist Functionality (E-commerce)

**Story:**

```text
As a Shopper,
I want to save products to a wishlist,
so that I can manage all items I'm interested in and purchase them at a convenient time.
```

**Why it works:**

- Actor is specific — a Shopper with a clear purchase intent context
- Action is outcome-focused — saving and managing interest, not "adding to a list"
- Value is concrete — deferred purchase on the shopper's own timeline

**Acceptance Criteria:**

```text
Done when: The shopper can add a product to their wishlist from the product detail page.
Done when: The shopper can view all items saved to their wishlist in one place.
Done when: The shopper can remove any item from their wishlist.
Done when: If an item in the wishlist goes out of stock, it is marked as "Out of Stock" but remains in the list.
Done when: The wishlist persists across sessions — items are still present when the user logs back in.
Done when: If the shopper is not logged in, they are prompted to log in or register before saving to wishlist.
```

---

## Example 6 — Community Safety Notification (Mobile App)

**Story:**

```text
As a Community Driver,
I want to warn my network about road hazards,
so that other drivers nearby can avoid the same danger I encountered.
```

**Why it works:**

- Actor is specific — Community Driver, not generic "user"
- Action is outcome-focused — warning the network, not "using voice commands" (mechanism removed)
- Value is immediate and personal — protecting peers from a hazard already experienced

**Acceptance Criteria:**

```text
Done when: The driver can create and publish a road hazard alert from within the app.
Done when: The app reads the alert back to the driver for confirmation before publishing.
Done when: The driver must confirm before the alert is sent to their network.
Done when: Upon confirmation, notifications are sent to all connected friends within 30 seconds.
Done when: If the driver cancels, no notification is sent and the draft is discarded.
Done when: If alert creation fails after 3 attempts, the app offers an alternative input method.
```

---

## Example 7 — Multi-Role Data Access

**Story:**

```text
As a CSR System User,
I want to update customer demographic data,
so that customer records remain accurate and up to date.
```

**Why it works:**

- Actor is a unified persona covering multiple roles — valid when all roles share the same build + test path
- Action is singular and clear — update demographic data
- Roles are separated in AC, not the story — keeping the story statement clean

**Acceptance Criteria:**

```text
Done when: A Customer Service Rep can update demographic data.
Done when: An Admin can update demographic data.
Done when: A Supervisor can update demographic data and view an audit log of all changes.
Done when: Each role's access is verified by individual login credentials before updates are permitted.
Done when: If a user attempts to access demographic data without the appropriate role, they receive an "Access Denied" message.
```

---

## Example 8 — API Story

**Story:**

```text
As the Orders API,
I want to include the order status and estimated delivery date in the response,
so that the customer-facing mobile app can display accurate delivery information to end users.
```

**Why it works:**

- Actor is the API itself — valid for system-to-system integration stories
- Action defines what data the API exposes — outcome for the consuming application
- Value traces to the end user — accurate delivery information reaches real people

**Acceptance Criteria:**

```text
Done when: The API response includes the fields: order_id, order_status, estimated_delivery_date, last_updated_timestamp.
Done when: The API returns a response within 300ms for 95% of requests under normal load.
Done when: If an order_id does not exist, the API returns a 404 status with the message "Order not found."
Done when: The API is accessible only to authenticated services with a valid API key.
Done when: The API response schema is documented and versioned.
```
