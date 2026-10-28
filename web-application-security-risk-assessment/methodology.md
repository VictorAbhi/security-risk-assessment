# Assessment Methodology

## 1. Overview

The assessment followed a structured manual security testing process.

The objective was to move beyond simply identifying technical vulnerabilities and evaluate their potential security risk to the application.

The assessment process was:

1. Understand the application
2. Identify assets
3. Identify vulnerabilities
4. Develop realistic threat scenarios
5. Analyze likelihood
6. Analyze impact
7. Determine risk
8. Recommend controls
9. Evaluate residual risk

---

## 2. Application Understanding

Initial testing focused on understanding the application's normal functionality.

This included:

- User registration and authentication
- Product browsing
- User Reviews
- Shopping baskets
- Password recovery
- Password changes
- Search
- Payment functionality for deluxe subscription

Understanding normal behavior was necessary before testing whether security controls could be bypassed.

---

## 3. Manual Security Testing

Manual testing was performed by interacting with the application and inspecting HTTP traffic.

Burp Suite was used to:

- Intercept requests
- Inspect HTTP parameters
- Modify requests
- Replay requests
- Observe application responses

Testing focused on determining whether security decisions were properly enforced by the server.

---

## 4. Vulnerability Categories

The assessment covered the following categories:

### Authentication

Testing whether authentication and password recovery mechanisms could be abused.

### Authorization

Testing whether users could access or modify resources belonging to other users.

### Input Validation

Testing whether application input was safely handled.

### Injection

Testing whether user-controlled input could influence backend queries or application behavior.

### Cross-Site Request Forgery

Testing whether sensitive actions could be triggered without appropriate authorization from the legitimate user.

### Business Logic

Testing whether application workflows could be bypassed by manipulating requests or parameters.

---

## 5. Risk Analysis

For each confirmed finding, likelihood and impact are assessed separately.

### Likelihood

Likelihood represents how feasible exploitation is under the tested conditions.

Factors considered include:

- Attacker access requirements
- Technical complexity
- User interaction
- Required knowledge
- Reliability of exploitation

### Impact

Impact represents the potential consequences of successful exploitation.

Factors considered include:

- Confidentiality impact
- Integrity impact
- Authentication impact
- Financial impact
- Number or type of affected users

### Risk

A simple qualitative model is used:

**Risk = Likelihood × Impact**

The resulting rating is used to prioritize remediation.