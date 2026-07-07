# Observed Issues and QA Recommendations

## 1. Overview

This document records observed usability points, testing risks, and QA recommendations identified during manual testing of the OpenMRS demo system.

No critical functional defect was found during the executed manual test cases. Therefore, this document focuses on improvement recommendations instead of fabricated bug reports.

## 2. Test Environment

| Item         | Description                                            |
| ------------ | ------------------------------------------------------ |
| Application  | OpenMRS Demo                                           |
| Testing Type | Manual Testing                                         |
| Browser      | Google Chrome                                          |
| Test Data    | Demo / dummy data                                      |
| Test Result  | 28 test cases executed, 28 passed, 0 failed, 0 blocked |

## 3. Observed Issues and Recommendations

### OBS_001 - Login location selection may not be obvious for first-time users

| Field                | Description                                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Type                 | Usability Improvement                                                                                                                            |
| Module               | Login                                                                                                                                            |
| Severity             | Low                                                                                                                                              |
| Priority             | Medium                                                                                                                                           |
| Observation          | The user must select a location before logging in. However, first-time users may not immediately understand that location selection is required. |
| Expected Improvement | The system should provide clearer guidance, such as a short note or validation message explaining that a location must be selected before login. |
| Recommendation       | Add a clear instruction near the location list, for example: “Please select a location before logging in.”                                       |
| Status               | Recommendation                                                                                                                                   |

---

### OBS_002 - Patient search depends heavily on existing demo data

| Field                | Description                                                                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type                 | Test Risk                                                                                                                                                                  |
| Module               | Patient Search                                                                                                                                                             |
| Severity             | Medium                                                                                                                                                                     |
| Priority             | Medium                                                                                                                                                                     |
| Observation          | Patient search results depend on the available demo data. If demo data changes, some manual or automated test cases may fail even when the function still works correctly. |
| Expected Improvement | Test data should be stable and predictable for regression testing.                                                                                                         |
| Recommendation       | Use fixed dummy patient data in a local OpenMRS environment, or clearly document the sample search keywords used during testing.                                           |
| Status               | Recommendation                                                                                                                                                             |

---

### OBS_003 - Validation messages should be checked more deeply in patient registration

| Field                | Description                                                                                                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type                 | Validation Improvement                                                                                                                                                                 |
| Module               | Register Patient                                                                                                                                                                       |
| Severity             | Low                                                                                                                                                                                    |
| Priority             | Medium                                                                                                                                                                                 |
| Observation          | Required field validation is displayed when mandatory information is missing, but the clarity and consistency of validation messages should be verified across all registration steps. |
| Expected Improvement | Each required field should have a clear and user-friendly validation message.                                                                                                          |
| Recommendation       | Add more negative test cases for missing name, gender, birthdate, address, and identifier fields.                                                                                      |
| Status               | Recommendation                                                                                                                                                                         |

---

### OBS_004 - Evidence is stored as general screenshots instead of one screenshot per test case

| Field                | Description                                                                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type                 | QA Documentation Improvement                                                                                                                                          |
| Module               | Test Evidence                                                                                                                                                         |
| Severity             | Low                                                                                                                                                                   |
| Priority             | Medium                                                                                                                                                                |
| Observation          | The project uses general screenshots to show main tested areas instead of capturing detailed evidence for every manual test case.                                     |
| Expected Improvement | Evidence should be easy to trace back to important test flows.                                                                                                        |
| Recommendation       | Keep the current general screenshots, but add a short note in the test summary explaining that screenshots are used as overview evidence, not per-test-case evidence. |
| Status               | Recommendation                                                                                                                                                        |

---

### OBS_005 - Demo environment may affect test stability

| Field                | Description                                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Type                 | Environment Risk                                                                                                                            |
| Module               | Overall System                                                                                                                              |
| Severity             | Medium                                                                                                                                      |
| Priority             | Medium                                                                                                                                      |
| Observation          | The OpenMRS demo environment is shared and may change over time. This can affect test data, system response, or automation reliability.     |
| Expected Improvement | A stable testing environment should be used for repeatable testing.                                                                         |
| Recommendation       | For future automation testing, set up a local OpenMRS instance or clearly document environment risks in the README and test summary report. |
| Status               | Recommendation                                                                                                                              |

## 4. Conclusion

During manual testing, no critical functional defect was identified. All executed test cases passed based on the defined expected results.

However, several QA recommendations were recorded to improve usability, validation coverage, test data stability, evidence management, and future automation reliability.
