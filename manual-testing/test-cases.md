# Manual Test Cases

The detailed manual test cases are maintained in:

```text
manual-testing/test_cases.xlsx
```

Recommended columns:

| Column | Purpose |
|---|---|
| Test Case ID | Unique test case identifier |
| Scenario ID | Link to `test-scenarios.md` |
| Module | Login, Logout, Patient Search, Patient Profile, Registration, API |
| Test Title | Short test objective |
| Pre-condition | Required starting state |
| Test Steps | Step-by-step execution |
| Test Data | Demo/dummy input data |
| Expected Result | Expected system behavior |
| Actual Result | Actual result after execution |
| Status | Pass / Fail / Blocked / Skipped |
| Priority | High / Medium / Low |
| Automation Candidate | Yes / No / Optional |
| API Candidate | Yes / No / Optional |
| Notes | Risks, limitations, or observations |

Evidence is stored separately under the `evidence/` folders. A case should be marked as `Pass` only when the result is backed by execution notes, screenshots, an automation report, or an API run result.

Use only public demo data or dummy data. Real patient data is not used.
