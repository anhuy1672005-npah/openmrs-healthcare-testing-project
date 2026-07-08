# Observed Issues and QA Recommendations

## 1. Overview

This document records observed usability points, testing risks, API observations, and QA recommendations identified during the OpenMRS O2 testing project.

This document separates confirmed test results from QA observations and recommendations. Items below are not presented as critical defects unless they have clear reproduction evidence.

## 2. Test Environment

| Item | Description |
|---|---|
| Application | OpenMRS O2 Demo / Reference Application 2.x |
| Testing Type | Manual test design, Selenium UI automation, Postman API testing |
| Browser | Google Chrome |
| Test Data | Public demo data / dummy data only |
| Execution Note | Not all 28 manual cases have direct evidence. Evidence-backed, blocked, skipped, and not-run statuses are tracked in `test_cases.xlsx`. |

## 3. Observed Issues and Recommendations

### OBS_001 - Login location selection may not be obvious for first-time users

| Field | Description |
|---|---|
| Type | Usability Improvement |
| Module | Login |
| Severity | Low |
| Priority | Medium |
| Observation | The user must select a location before logging in. First-time users may not immediately understand that location selection is required. |
| Expected Improvement | The system should provide clearer guidance or validation text near the location list. |
| Recommendation | Add a clear instruction such as: “Please select a location before logging in.” |
| Status | Recommendation |

---

### OBS_002 - Patient search depends heavily on existing demo data

| Field | Description |
|---|---|
| Type | Test Risk |
| Module | Patient Search |
| Severity | Medium |
| Priority | Medium |
| Observation | Patient search results depend on available public demo data. If demo data changes, manual or automated tests may skip or fail even when the feature still works correctly. |
| Expected Improvement | Regression testing should use stable and predictable data. |
| Recommendation | Use fixed dummy patient data in a local OpenMRS environment, or document the exact search keyword used during execution. |
| Status | Recommendation |

---

### OBS_003 - Registration validation should be verified more deeply in a stable environment

| Field | Description |
|---|---|
| Type | Validation Improvement |
| Module | Register Patient |
| Severity | Low |
| Priority | Medium |
| Observation | Required-field validation scenarios are designed, but full validation coverage should not be overstated on the shared public demo because registration can create data and wizard behavior may vary. |
| Expected Improvement | Each required field should have a clear and user-friendly validation message. |
| Recommendation | Execute missing-name, missing-gender, birthdate, address, and confirmation-step validation on a local or controlled OpenMRS instance. |
| Status | Recommendation |

---

### OBS_004 - Manual evidence is overview-based, not one screenshot per test case

| Field | Description |
|---|---|
| Type | QA Documentation Improvement |
| Module | Test Evidence |
| Severity | Low |
| Priority | Medium |
| Observation | The project stores automation/API evidence and may store general manual screenshots, but it does not currently provide one manual screenshot for every test case. |
| Expected Improvement | Important manual flows should be traceable to screenshots or notes when marked as executed. |
| Recommendation | Add at least five manual screenshots for login pass, invalid login, logout, no-result search, and registration validation if those cases are marked as executed. |
| Status | Recommendation |

---

### OBS_005 - Public demo environment may affect test stability

| Field | Description |
|---|---|
| Type | Environment Risk |
| Module | Overall System |
| Severity | Medium |
| Priority | Medium |
| Observation | The OpenMRS O2 public demo is shared and may change over time. This can affect test data, system response, API behavior, or automation reliability. |
| Expected Improvement | A stable testing environment should be used for repeatable regression testing. |
| Recommendation | For future automation testing, set up a local OpenMRS instance or clearly document environment risks in README and test summary. |
| Status | Recommendation |

---

### OBS_006 - Invalid patient UUID may return server error instead of client error

| Field | Description |
|---|---|
| Type | API Robustness Observation |
| Module | Patient API |
| Severity | Medium |
| Priority | Medium |
| Observation | The public O2 demo may return `500` when requesting a patient with an invalid UUID. In stricter API behavior, `400` or `404` would be more appropriate. |
| Expected Improvement | Invalid client input should return a clear client-side error response. |
| Recommendation | Keep this as an API observation in Postman results and avoid presenting it as a strict product pass. |
| Status | Observation |

---

### OBS_007 - No-auth patient search may return 200 on the public demo

| Field | Description |
|---|---|
| Type | API Access-Control Observation |
| Module | Patient API |
| Severity | Medium |
| Priority | Medium |
| Observation | Patient search without Basic Auth may return `200` depending on public demo configuration. In stricter environments, a no-auth request would usually return `401` or `403`. |
| Expected Improvement | Protected patient resources should have clear and consistent authorization behavior. |
| Recommendation | Document this as a public-demo configuration/access-control observation and verify again on a controlled environment before filing a security bug. |
| Status | Observation |

## 4. Conclusion

The project does not claim that every designed manual test case passed. It separates evidence-backed results from blocked, skipped, and not-run cases so the report remains consistent with actual execution scope.
