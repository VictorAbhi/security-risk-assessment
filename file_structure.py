from pathlib import Path

# Project root
project = Path("web-application-security-risk-assessment")

# Directories
findings = project / "findings"
evidence = project / "evidence"

# Create directories
findings.mkdir(parents=True, exist_ok=True)
evidence.mkdir(parents=True, exist_ok=True)

# Files to create
files = {
    project / "README.md": """# Web Application Security Risk Assessment

Security assessment of OWASP Juice Shop performed in a controlled lab environment.

## Findings

- Broken Authentication
- Broken Access Control
- SQL Injection
- XSS
- CSRF
- Payment Bypass
""",

    project / "risk-register.md": """# Risk Register

| ID | Risk | Likelihood | Impact | Rating | Status |
|---|---|---:|---:|---|---|
| R-01 | Broken Authentication | TBD | TBD | TBD | Open |
| R-02 | Broken Access Control | TBD | TBD | TBD | Open |
| R-03 | SQL Injection | TBD | TBD | TBD | Open |
| R-04 | XSS | TBD | TBD | TBD | Open |
| R-05 | CSRF | TBD | TBD | TBD | Open |
| R-06 | Payment Bypass | TBD | TBD | TBD | Open |
""",

    findings / "broken-authentication.md": "# R-01 — Broken Authentication\n\n",
    findings / "broken-access-control.md": "# R-02 — Broken Access Control\n\n",
    findings / "sql-injection.md": "# R-03 — SQL Injection\n\n",
    findings / "xss.md": "# R-04 — Cross-Site Scripting (XSS)\n\n",
    findings / "csrf.md": "# R-05 — Cross-Site Request Forgery (CSRF)\n\n",
    findings / "payment-bypass.md": "# R-06 — Payment Bypass\n\n",
}

# Create files
for file_path, content in files.items():
    file_path.write_text(content, encoding="utf-8")

print(f"Created project: {project.resolve()}")