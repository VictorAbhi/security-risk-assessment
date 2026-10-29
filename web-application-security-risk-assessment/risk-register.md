# Risk Register

| ID | Finding | Asset / Function | Likelihood | Impact | Risk | Priority |
|---|---|---|---|---|---|---|
| R-01 | Broken Authentication / Account Takeover / Information Disclosure | User accounts / password recovery | High | High | Critical | Critical |
| R-02 | Cross-Site Scripting (XSS) | Search functionality / user browser | Medium | Medium | Medium | Medium |
| R-03 | Password Change via CSRF | User accounts / password change | High | High | Critical | Critical |
| R-04 | SQL Injection in Login | Authentication / application database | High | High | Critical | Critical |
| R-05 | Payment Validation Bypass | Payment processing / orders | High | High | Critical | Critical |
| R-06 | Unauthorized Basket Access | User shopping baskets | Medium | Medium | Medium | Medium |

---

## R-02 — Cross-Site Scripting (XSS)

**Risk:** Medium

A malicious JavaScript payload was submitted through the application's search functionality.

The application processed the injected input in a way that allowed JavaScript execution in the browser.

The final severity depends on whether the vulnerability is reflected, stored, or DOM-based and whether another user's browser can be affected.

**Current evidence:** JavaScript execution was demonstrated through a malicious search input.

---

## R-03 — Password Change via CSRF

**Risk:** Critical

The password-change functionality can be triggered through a Cross-Site Request Forgery attack.

The tested request allows the current password parameter to be removed, while a victim can be induced to submit a request that changes the account password.

If successfully exploited against an authenticated victim, this can result in account takeover.

This finding represents an attack chain involving both insufficient protection of a sensitive state-changing operation and CSRF.

---

## R-04 — SQL Injection in Login

**Risk:** Critical

The login functionality was found to be vulnerable to SQL injection.

An attacker can manipulate the login input to alter the backend authentication query and bypass normal password authentication.

The demonstrated impact is authentication bypass.

No claim of complete database compromise is made unless additional database access was demonstrated.

---

## R-05 — Payment Validation Bypass

**Risk:** Critical

The payment workflow does not sufficiently validate the selected payment method on the server side.

By modifying the HTTP request and submitting:

`paymentMode=none`

the payment process can be bypassed.

This represents a business-logic and server-side validation weakness.

The potential impact includes unauthorized completion of transactions without satisfying the expected payment requirements.

---

## R-06 — Unauthorized Basket Access

**Risk:** Medium

The application does not properly enforce authorization when accessing basket information.

By manipulating a user-controlled identifier, it was possible to access another user's basket.

This represents a broken access control vulnerability similar to an IDOR/BOLA condition.

The vulnerability affects the confidentiality of users' shopping information and demonstrates that the server is relying on a client-controlled identifier without adequately verifying ownership.

---

# Risk Prioritization

Based on the current assessment, remediation should be prioritized as follows:

### Priority 1 — Critical

- R-03 — Password Change via CSRF
- R-04 — SQL Injection in Login
- R-05 — Payment Validation Bypass

These findings can directly affect account security, authentication, or transaction integrity.

### Priority 2 — High

- R-01 — Weak Password Recovery / Account Enumeration

The finding affects authentication security. Its final severity should be reassessed if full password-reset/account-takeover impact is demonstrated.

### Priority 3 — Medium

- R-02 — Cross-Site Scripting
- R-06 — Unauthorized Basket Access

These findings can affect users and application data, but their final severity depends on exploitability and demonstrated impact.

---

## Risk Rating Notes

The ratings above are preliminary.

Final ratings should be reviewed after documenting:

- Exact exploitation steps
- Required attacker privileges
- Required victim interaction
- Confidentiality impact
- Integrity impact
- Potential number of affected users
- Whether exploitation can be automated
- Whether the demonstrated impact represents the maximum realistic impact

The final assessment should distinguish between **demonstrated impact** and **potential impact**.