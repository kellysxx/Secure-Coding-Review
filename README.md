# Secure-Coding-Review

A small Python and SQLite practice project reviewing SQL query construction.

## Purpose

This project demonstrates how building a SQL query by joining user input into a string can create a SQL injection risk, and how parameterized queries help prevent it.

## Files

- `insecure_original.py` — intentionally vulnerable example for review practice.
- `app.py` — corrected example that uses a parameterized query and closes the database connection.
- `review_notes.md` — review scope, finding, remediation, and limitations.
- `Secure_Coding_Review_Report.docx` — report for the exercise.
- `evidence/` — screenshots of the initial Bandit finding and follow-up scan.

## Static analysis

The project was reviewed with Bandit. The initial scan flagged the dynamically constructed SQL query (B608). After changing it to use a parameterized query, the follow-up scan reported no issues identified.

To run Bandit:

```bash
python -m bandit insecure_original.py
python -m bandit app.py
