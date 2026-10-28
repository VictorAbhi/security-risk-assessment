# Scope and Objectives

## 1. Assessment Scope

The assessment targets the OWASP Juice Shop web application.

The primary objective is to identify security weaknesses affecting the confidentiality, integrity, and availability of application resources, with particular attention to authentication, authorization, input handling, and business logic.

---

## 2. Assets

The following assets were considered during the assessment:

| Asset | Security Objective |
|---|---|
| User accounts | Confidentiality and integrity |
| User credentials | Confidentiality |
| Password recovery functionality | Authentication integrity |
| User personal information | Confidentiality |
| Shopping baskets | Confidentiality and integrity |
| Orders and payment information | Integrity and confidentiality |
| Product information | Integrity |
| Application functionality | Integrity and availability |
| Authentication/session mechanisms | Confidentiality and integrity |

---

## 3. Security Objectives

The assessment considers three primary security objectives.

### Confidentiality

Unauthorized users should not be able to access information belonging to other users.

Examples include:

- User information
- Credentials
- Shopping baskets
- Orders

### Integrity

Users should not be able to modify application data or perform actions they are not authorized to perform.

Examples include:

- Changing another user's account information
- Modifying another user's basket
- Bypassing payment validation

### Availability

Application functionality should remain available to legitimate users.

Availability testing was not a primary focus of this assessment.

---

## 4. Testing Objectives

The assessment aims to determine whether an attacker can:

- Circumvent authentication mechanisms
- Abuse password recovery functionality
- Execute malicious client-side code
- Manipulate database queries
- Perform unauthorized actions
- Access another user's data
- Circumvent payment controls
- Exploit application trust in user-controlled input

---

## 5. Assessment Limitations

The assessment represents a focused manual review rather than a complete penetration test.

Only vulnerabilities that were identified and reproduced during the assessment are documented.

No assumption is made that untested functionality is secure.