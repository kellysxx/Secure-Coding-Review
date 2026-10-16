# Secure Coding Review

A Python and SQLite practice project reviewing a SQL injection risk and its remediation.

## Project overview

The original example builds a SQL query by joining a name value into the query string. This can allow input to change the query’s meaning. The corrected example uses a parameterized query.

## Review result

| Item | Result |
|---|---|
| Finding | SQL query assembled with string concatenation |
| Tool | Bandit |
| Initial result | B608 reported; medium severity, low confidence |
| Remediation | Replaced string concatenation with a parameterized query |
| Follow-up scan | Bandit reported no issues identified in the scanned file |

A clean Bandit scan does not prove that an entire application is secure.

## Project files

- `insecure_original.py` — intentionally vulnerable sample used for review practice.
- `app.py` — corrected sample using a parameterized query.
- `review_notes.md` — scope, method, finding, remediation, and limitations.

## Reproduce the scans

In Kali, open a terminal in the project folder and activate your virtual environment:

```bash
source .venv/bin/activate

**Run Bandit against the original and corrected files:**
python -m bandit insecure_original.py
python -m bandit app.py

**## Scope and limitations**
This was a small local learning exercise. No employer code, production service, external system, or real user data was reviewed. Bandit checks selected patterns and may miss issues outside its rules. This work is not a full application security audit.
Author
KELECHI HAPPINESS UZOMA
Intern, CODEALPHA
20 October 2026
