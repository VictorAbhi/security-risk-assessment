# R-01 — Broken Authentication
 — Account Takeover Through OSINT

**Risk Rating:** Critical  
**Category:** Broken Authentication / Account Takeover / Information Disclosure  
**Affected Functionality:** User accounts and Forgot Password

---

## 1. Description

The application's password recovery mechanism can be abused to take over user accounts.

During the assessment, a user's email address was identified through publicly accessible information within the application. The account's security-question answer was then obtained through OSINT.

The discovered information was sufficient to complete the password recovery process and gain access to the user's account without knowing the original password.

This demonstrates that the password recovery mechanism relies on information that can be obtained by an attacker rather than requiring a sufficiently strong, secret recovery factor.

The vulnerability therefore allows an attacker to transition from publicly available information to **unauthorized account access**.

---

## 2. Affected Asset

The primary affected asset is the **user account authentication mechanism**.

Potentially affected resources include:

- User accounts
- Account credentials
- Personal information
- Shopping baskets
- Orders
- Account-related functionality
- Any other resources accessible to the compromised account

---

## 3. Evidence

### Step 1 — Discovering the Target User

User information was identified through publicly accessible product reviews within the application.

The review information exposed the user's email address.

**Evidence:**  

---

### Step 2 — Initiating Password Recovery

The discovered email address was submitted to the application's **Forgot Password** functionality.

The application proceeded with the recovery process for the identified account.

**Evidence:**  
`[Insert Screenshot — password recovery using discovered email address]`

---

### Step 3 — Obtaining the Security Question Answer Through OSINT

The security-question answer associated with the target account was identified using publicly available information obtained through OSINT.

The answer was sufficiently predictable/discoverable that an attacker did not need access to the victim's existing password.

**Evidence:**  
`[Insert Screenshot — OSINT source revealing the security-question answer]`

> Sensitive information from the OSINT source should be redacted where appropriate in the published report.

---

### Step 4 — Completing Password Recovery

The discovered security-question answer was submitted to the password recovery mechanism.

The recovery process accepted the answer and allowed the account password to be changed.

**Evidence:**  
`[Insert Screenshot — successful password reset]`

---

### Step 5 — Account Takeover

The newly established password was used to authenticate to the victim's account.

This confirmed that the password recovery weakness could be used to achieve **full account takeover**.

**Evidence:**  
`[Insert Screenshot — successful authentication to the compromised account]`

---

## 4. Attack Scenario

A realistic attack scenario is:

1. The attacker identifies a target user through publicly accessible application information.
2. The attacker obtains the user's email address.
3. The attacker initiates the password recovery process via Forgot Password in Login functionality.
4. The application presents a security question.
5. The attacker searches publicly available information using OSINT techniques.
6. The attacker discovers the answer to the security question.
7. The attacker submits the discovered answer to the password recovery mechanism.
8. The application allows the attacker to set a new password.
9. The attacker authenticates using the new password.
10. The attacker gains control of the victim's account.

This attack does not require knowledge of the victim's original password.

---

## 5. Impact

The demonstrated impact is **account takeover**.

An attacker who successfully exploits this weakness can gain unauthorized access to a victim's account and potentially access or modify resources available to that account.

Potential consequences include:

- Unauthorized access to personal information
- Unauthorized access to shopping baskets
- Unauthorized access to order information
- Modification of account information
- Modification of the victim's password
- Loss of account availability to the legitimate user
- Potential abuse of functionality available to the compromised account

The severity may be greater if the compromised account has access to sensitive information or privileged functionality.

---

## 6. Likelihood

**Likelihood: High**

The attack does not require exploitation of a complex technical vulnerability.

The demonstrated attack chain relies on:

- Information exposed through application functionality
- Publicly available information
- A weak account-recovery mechanism

Once the required information is obtained, the password recovery process can be completed without knowing the victim's original password.

OSINT techniques can also be performed remotely and may require little interaction with the target.

Therefore, successful exploitation is considered reasonably feasible.

---

## 7. Risk Assessment

**Impact:** High  
**Likelihood:** High  
**Overall Risk:** Critical

The vulnerability is rated **Critical** because it allows an attacker to take over a user account without knowing the legitimate password.

The attack combines information disclosure and weak authentication controls to bypass the intended authentication boundary.

The demonstrated end result is unauthorized access to the victim's account.

---

## 8. Root Cause

The primary root cause is the use of a **security question as a password-recovery authentication factor** when the answer can be discovered through publicly available information.

Additional contributing factors include:

- Exposure of user-identifying information through application functionality
- Reliance on knowledge-based authentication
- Insufficient protection of the password recovery process
- Lack of a strong, secret, time-limited recovery mechanism

The security question does not provide sufficient assurance that the person requesting the password reset is the legitimate account owner.

---

## 9. Recommended Remediation

### 1. Replace security questions

Security questions should not be used as the primary authentication factor for password recovery.

Instead, use a secure password-reset mechanism based on a verified recovery channel.

For example:

- Cryptographically random reset token
- Short expiration period
- Single-use token
- Verified email address or other appropriate recovery factor

---

### 2. Do not expose user email addresses unnecessarily

User email addresses should not be publicly disclosed through reviews or other application functionality.

Use a non-sensitive username or pseudonymous identifier where possible.

---

### 3. Implement rate limiting

Password recovery attempts should be rate-limited to reduce automated attacks and repeated guessing attempts.

---

### 4. Prevent account enumeration

The application should avoid revealing whether an email address corresponds to an existing account.

Password recovery responses should use generic messages that do not disclose account existence.

---

### 5. Require additional verification for sensitive recovery actions

Password changes following account recovery should require an appropriately strong verification mechanism.

Where risk warrants it, additional authentication or step-up verification should be considered.

---

### 6. Monitor account recovery activity

Security monitoring should identify:

- Repeated password recovery attempts
- Password resets from unusual locations or devices
- Multiple accounts targeted from the same source
- Password resets followed by unusual account activity
- Changes to account information immediately following recovery

---

## 10. Detection and Monitoring

Relevant security events should be logged and correlated across authentication and account-management systems.

Potential indicators of compromise include:

- Multiple password-recovery attempts
- Password reset followed by login from a new device
- Password reset followed by changes to account information
- Multiple accounts targeted from a common source
- Unusual access immediately after a password reset

These events can be used to identify potential account-takeover activity.

---

## 11. Residual Risk

After remediation, the residual risk should be reduced through:

- Removal of security questions as an authentication factor
- Secure, single-use password-reset tokens
- Protection of user-identifying information
- Rate limiting
- Account-enumeration protections
- Monitoring of password recovery and post-recovery activity

The effectiveness of these controls should be validated through a follow-up security test attempting to reproduce the original account-takeover scenario.

---

## 12. Evidence Summary

| Evidence | Description |
|---|---|
| E-01 | User email address identified through publicly accessible application information |
| E-02 | Email address submitted to the password recovery functionality |
| E-03 | Security-question answer obtained through OSINT