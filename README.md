# Secure Coding Review

A Python and SQLite practice project demonstrating how to identify and remediate a SQL injection risk.

## Overview

The original sample builds a SQL query by joining a name value into the query string. If that value is user controlled, it could alter the query. The corrected sample uses a parameterized query so the input is handled as data.

## Finding and fix

| Review item | Result |
| --- | --- |
| Finding | SQL query constructed with string concatenation |
| Static analysis | Bandit reported B608, medium severity and low confidence |
| Remediation | Replaced concatenation with a parameterized query |
| Rescan | Bandit reported no issues in the corrected file |

A clean Bandit scan does not prove that an entire application is secure.

## Project files

- `insecure_original.py` — intentionally vulnerable learning example.
- `app.py` — corrected example using a parameterized query.
- `review_notes.md` — scope, review method, finding, remediation, and limitations.

## Run the scan in Kali

From the project folder, create and activate a virtual environment, then install Bandit:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install bandit

Scan the original and corrected examples:
python -m bandit insecure_original.py
python -m bandit app.py

Scope and limitations
This was a small local learning exercise. No employer code, production service, external system, or real user data was reviewed. Bandit checks selected patterns and may miss issues outside its rules. This exercise is not a full application security audit.

Author

KELECHI HAPPINESS UZOMA
Intern, CODEALPHA
20 October 2026

