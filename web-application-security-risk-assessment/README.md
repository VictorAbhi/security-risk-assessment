# Web Application Security Risk Assessment

## Overview

This project documents a security assessment of the OWASP Juice Shop application, a deliberately vulnerable web application designed for security testing and education.

The assessment focuses on identifying common web application security risks, evaluating their potential impact, and translating technical vulnerabilities into security risks.

The assessment covers:

- Authentication and password recovery
- Authorization and access control
- Cross-Site Scripting (XSS)
- SQL Injection
- Cross-Site Request Forgery (CSRF)
- Business logic and payment validation
- User and basket data protection

The objective is not only to identify vulnerabilities, but also to understand:

**Asset → Threat → Vulnerability → Risk → Impact → Control → Residual Risk**

---

## Scope

The assessment was performed against the OWASP Juice Shop web application.

### In Scope

- Authentication mechanisms
- Password recovery functionality
- Password change functionality
- User authorization
- Basket/cart access
- Search functionality
- Login functionality
- Payment processing
- HTTP requests and responses
- Application input handling

### Out of Scope

- Denial-of-service testing
- Attacks against external systems
- Social engineering
- Physical security
- Infrastructure outside the Juice Shop environment

---

## Methodology

The assessment used a manual application security testing approach.

The main techniques included:

- Application functionality analysis
- Browser-based testing
- HTTP request and response inspection
- Burp Suite
- Controlled manipulation of HTTP parameters
- Authentication and authorization testing
- Input validation testing
- Business logic testing

Identified vulnerabilities were evaluated according to their potential likelihood and impact.

---

## Findings

| ID | Finding | Category | Risk |
|---|---|---|---|
| R-01 | Weak Password Recovery / Account Enumeration | Authentication | TBD |
| R-02 | Cross-Site Scripting (XSS) | Input Validation | TBD |
| R-03 | Password Change via CSRF | Access Control / CSRF | TBD |
| R-04 | SQL Injection in Login | Injection / Authentication | TBD |
| R-05 | Payment Validation Bypass | Business Logic | TBD |
| R-06 | Unauthorized Basket Access | Broken Access Control / IDOR | TBD |

> Risk ratings will be finalized after completing the individual risk analysis.

---

## Risk Assessment Approach

Each finding will be analyzed using:

- Affected asset
- Vulnerability
- Threat scenario
- Evidence
- Likelihood
- Impact
- Risk rating
- Root cause
- Recommended remediation
- Detection and monitoring
- Residual risk

The assessment uses a simple risk model:

**Risk = Likelihood × Impact**

The purpose is to prioritize vulnerabilities according to the potential security consequences rather than treating every vulnerability as equally important.

---

## Evidence

Evidence screenshots and supporting material are stored in the `evidence/` directory.

Only relevant evidence is included to demonstrate:

1. The security weakness
2. The resulting security impact, where demonstrated

---

## Disclaimer

This assessment was performed against the intentionally vulnerable OWASP Juice Shop application in a controlled environment for educational and cybersecurity development purposes. Moreover, This assessment is for my learning purpose(starting point) to know the cybersecurity business. Nowadays, everything is being automated, this is just a small start to understand how business works.