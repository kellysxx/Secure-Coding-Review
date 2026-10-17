# Review notes

## Scope and authorization
Reviewed a five-line local Python example with SQLite query construction. No production service, company repository, external system, or real user data was involved. The exercise is suitable as a practice demonstration. A workplace audit should begin only after a supervisor assigns an authorized repository and scope.

## Method
1. Ran Bandit against the original Python sample.
2. Examined the query construction at `insecure_original.py` line 6.
3. Assessed the issue manually: the supplied name was concatenated into SQL syntax.
4. Replaced concatenation with a parameter placeholder and separately supplied the value.
5. Reran Bandit against the corrected sample.

## Finding F-01: SQL injection risk from dynamic query construction
- **Severity:** Medium (as reported by Bandit)
- **Confidence:** Low (as reported by Bandit; confirm in application context)
- **Affected code:** `insecure_original.py`, query construction in `find_user`
- **Evidence:** Bandit reported B608 for a hardcoded SQL expression. The exercise screenshots show the initial finding.
- **Risk:** If a value controlled by a user is joined into SQL text, crafted input may change the meaning of the query. Actual impact depends on the application context and database permissions.
- **Recommendation:** Bind values with the database driver's parameter interface. Do not concatenate untrusted input into a query.
- **Remediation:** The corrected `app.py` uses `WHERE name = ?` and passes `(name,)` separately to `execute()`.The current sample does not show explicit connection cleanup; a production implementation should close the connection reliably, for example with a finally block or a context manager.
- **Verification:** The follow-up Bandit screenshot reports “No issues identified.” This confirms no Bandit findings for the scanned file, not that the whole application is secure.

## Additional secure coding recommendations
- Use least-privilege database accounts and restrict access to database files.
- Validate input according to business rules; validation complements but does not replace parameterization.
- Avoid returning sensitive database or exception details to users.
- Review authentication, authorization, secrets handling, dependencies, logging, and error handling in a real application.
- Track findings with an owner, remediation status, and verification evidence in a workplace review.

## Limitations
This is a very small example. Bandit covers selected Python patterns and can produce false positives or miss issues outside its rules. The exercise did not include a full threat model, dependency audit, runtime assessment, or review of a larger application.

## Evidence for submission
Attach the screenshot showing Bandit's original B608 finding and the screenshot showing the clean rescan. Replace the author and organization placeholders in the report before submitting. Do not include employer code or internal findings unless approved.
