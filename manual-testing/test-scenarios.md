# Test Scenarios

## 1. Overview

This document defines the high-level test scenarios for the OpenMRS Healthcare Web Testing Project.

The scenarios are based on the application exploration notes from `application-map.md` and focus on the main workflows in scope:

* Login
* Logout
* Patient Search
* Patient Profile
* Patient Registration
* Form Validation
* Basic API-related workflows

These test scenarios will be used as the basis for writing detailed manual test cases, selecting Selenium UI automation candidates, and identifying related Postman API test cases.

---

## 2. Test Scenario Summary

| Module               | Number of Scenarios | Main Purpose                                    |
| -------------------- | ------------------: | ----------------------------------------------- |
| Login                |                   5 | Verify authentication and login validation      |
| Logout               |                   2 | Verify session ending behavior                  |
| Patient Search       |                   5 | Verify patient lookup behavior                  |
| Patient Profile      |                   3 | Verify patient detail display                   |
| Patient Registration |                   5 | Verify patient creation and form validation     |
| API-related Flows    |                   4 | Verify backend behavior related to UI workflows |
| Total                |                  24 | Covered key OpenMRS workflows in project scope  |

---

## 3. Login Scenarios

| Scenario ID  | Module | Scenario Description                                                    | Test Type | Priority | Automation Candidate | API Candidate |
| ------------ | ------ | ----------------------------------------------------------------------- | --------- | -------- | -------------------- | ------------- |
| SC_LOGIN_001 | Login  | Verify login with valid username, valid password, and selected location | Positive  | High     | Yes                  | Yes           |
| SC_LOGIN_002 | Login  | Verify login with invalid password                                      | Negative  | High     | Yes                  | Yes           |
| SC_LOGIN_003 | Login  | Verify login with empty username                                        | Negative  | Medium   | Yes                  | No            |
| SC_LOGIN_004 | Login  | Verify login with empty password                                        | Negative  | Medium   | Yes                  | No            |
| SC_LOGIN_005 | Login  | Verify login without selecting a location                               | Negative  | Medium   | Yes                  | No            |

### Notes

Login is a critical workflow because users must authenticate before accessing patient records. Login scenarios are good candidates for Selenium automation because they are stable, repeatable, and important for regression testing.

---

## 4. Logout Scenarios

| Scenario ID   | Module | Scenario Description                                   | Test Type                   | Priority | Automation Candidate | API Candidate |
| ------------- | ------ | ------------------------------------------------------ | --------------------------- | -------- | -------------------- | ------------- |
| SC_LOGOUT_001 | Logout | Verify user can log out successfully after login       | Positive                    | High     | Yes                  | Yes           |
| SC_LOGOUT_002 | Logout | Verify user cannot access protected pages after logout | Negative / Security-related | Medium   | Optional             | Yes           |

### Notes

Logout scenarios help verify session handling. These scenarios are useful for both UI testing and API/session testing.

---

## 5. Patient Search Scenarios

| Scenario ID   | Module         | Scenario Description                                          | Test Type           | Priority | Automation Candidate | API Candidate |
| ------------- | -------------- | ------------------------------------------------------------- | ------------------- | -------- | -------------------- | ------------- |
| SC_SEARCH_001 | Patient Search | Verify searching patient by valid patient name                | Positive            | High     | Yes                  | Yes           |
| SC_SEARCH_002 | Patient Search | Verify searching patient by valid patient identifier          | Positive            | High     | Yes                  | Yes           |
| SC_SEARCH_003 | Patient Search | Verify searching with a non-existing keyword                  | Negative            | Medium   | Yes                  | Yes           |
| SC_SEARCH_004 | Patient Search | Verify behavior when search input is empty                    | Negative / Boundary | Medium   | Optional             | Optional      |
| SC_SEARCH_005 | Patient Search | Verify behavior when search input contains special characters | Negative            | Medium   | Optional             | Yes           |

### Notes

Patient Search is one of the most important workflows in a healthcare application. Incorrect search behavior may cause users to open the wrong patient profile or fail to find the correct patient. This module should be covered by manual testing, Selenium automation, and API testing.

---

## 6. Patient Profile Scenarios

| Scenario ID    | Module          | Scenario Description                                                         | Test Type | Priority | Automation Candidate | API Candidate |
| -------------- | --------------- | ---------------------------------------------------------------------------- | --------- | -------- | -------------------- | ------------- |
| SC_PROFILE_001 | Patient Profile | Verify patient profile opens after selecting a patient from search results   | Positive  | High     | Yes                  | Yes           |
| SC_PROFILE_002 | Patient Profile | Verify patient name and patient identifier are displayed on the profile page | Positive  | High     | Yes                  | Yes           |
| SC_PROFILE_003 | Patient Profile | Verify basic patient demographic information is displayed correctly          | Positive  | Medium   | Optional             | Yes           |

### Notes

Patient Profile scenarios verify whether the system displays the correct patient information after a search action. These scenarios are important because profile information is directly related to patient data accuracy.

---

## 7. Patient Registration Scenarios

| Scenario ID     | Module           | Scenario Description                                      | Test Type             | Priority | Automation Candidate | API Candidate |
| --------------- | ---------------- | --------------------------------------------------------- | --------------------- | -------- | -------------------- | ------------- |
| SC_REGISTER_001 | Register Patient | Verify registering a new patient with valid required data | Positive              | High     | Optional             | Optional      |
| SC_REGISTER_002 | Register Patient | Verify required validation when given name is missing     | Negative / Validation | High     | Yes                  | Optional      |
| SC_REGISTER_003 | Register Patient | Verify required validation when family name is missing    | Negative / Validation | High     | Yes                  | Optional      |
| SC_REGISTER_004 | Register Patient | Verify required validation when gender is missing         | Negative / Validation | High     | Yes                  | Optional      |
| SC_REGISTER_005 | Register Patient | Verify behavior when invalid birthdate or age is entered  | Negative / Validation | Medium   | Optional             | Optional      |

### Notes

Patient Registration is a suitable module for manual testing because it includes multiple form fields and validation rules. It can also be partially automated, especially required field validation. Full patient creation automation should be handled carefully on the public demo environment to avoid creating too much unnecessary test data.

---

## 8. API-related Scenarios

| Scenario ID | Module             | Scenario Description                                                      | Test Type | Priority | Automation Candidate | API Candidate |
| ----------- | ------------------ | ------------------------------------------------------------------------- | --------- | -------- | -------------------- | ------------- |
| SC_API_001  | API Authentication | Verify API session or authentication check with valid credentials         | Positive  | High     | No                   | Yes           |
| SC_API_002  | API Current User   | Verify current authenticated user information is returned                 | Positive  | Medium   | No                   | Yes           |
| SC_API_003  | API Patient Search | Verify patient/person search API returns matching results                 | Positive  | High     | No                   | Yes           |
| SC_API_004  | API Negative Case  | Verify unauthorized or invalid UUID request returns proper error response | Negative  | High     | No                   | Yes           |

### Notes

API-related scenarios are included to connect UI workflows with backend behavior. These scenarios will be implemented in Postman rather than Selenium.

---

## 9. Automation Candidate Summary

| Scenario Group        | Recommended Automation Level | Reason                                                              |
| --------------------- | ---------------------------- | ------------------------------------------------------------------- |
| Login                 | High                         | Stable, repeatable, critical for regression                         |
| Logout                | Medium                       | Useful for authentication/session regression                        |
| Patient Search        | High                         | Important workflow and easy to assert                               |
| Patient Profile       | Medium                       | Useful when stable patient data is available                        |
| Patient Registration  | Medium / Optional            | Form validation is suitable, but full creation may affect demo data |
| API-related Scenarios | Postman only                 | Should be tested at API level, not Selenium                         |

---

## 10. Priority Definition

| Priority | Meaning                                                               |
| -------- | --------------------------------------------------------------------- |
| High     | Critical workflow or important validation that should be tested first |
| Medium   | Important but not as critical as core access/search workflows         |
| Low      | Nice-to-have scenario or less important edge case                     |

---

## 11. Test Type Definition

| Test Type        | Meaning                                                                    |
| ---------------- | -------------------------------------------------------------------------- |
| Positive         | Verifies that the system works correctly with valid input                  |
| Negative         | Verifies that the system handles invalid input or invalid actions properly |
| Validation       | Checks required fields, input rules, and error messages                    |
| Boundary         | Checks edge cases such as empty input                                      |
| Security-related | Basic check related to session or unauthorized access                      |

---

## 12. Next Step

The next step is to create detailed manual test cases based on these scenarios.

Each scenario will be expanded into one or more test cases with:

* Test Case ID
* Preconditions
* Test Steps
* Test Data
* Expected Result
* Actual Result
* Status
* Priority
* Severity
* Automation Candidate
* Evidence

