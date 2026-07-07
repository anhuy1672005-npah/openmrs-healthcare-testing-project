# Traceability Matrix

## 1. Overview

This traceability matrix maps manual test cases to planned Selenium UI automation and Postman API testing.

The purpose of this document is to show which manual test cases are suitable for automation and how they connect to the overall QA workflow.

Automation is not applied to every manual test case. Only stable, repeatable, high-priority, and easy-to-assert test cases are selected for the first automation scope.

## 2. Automation Selection Criteria

A test case is selected for Selenium automation when it meets most of the following criteria:

| Criteria                             | Description                                                    |
| ------------------------------------ | -------------------------------------------------------------- |
| High business value                  | The test case covers an important user flow.                   |
| Repeatable                           | The test case is useful for regression testing.                |
| Stable UI flow                       | The page and elements are not expected to change frequently.   |
| Clear expected result                | The result can be verified by assertion.                       |
| Low dependency on changing demo data | The test does not depend heavily on unstable public demo data. |

## 3. Selected Automation Scope

| Requirement / Flow                      | Manual Test Case ID | Module           | Automation Priority | Selenium Test File                 | Page Object Class                     | API Candidate | Status   | Notes                                           |
| --------------------------------------- | ------------------- | ---------------- | ------------------- | ---------------------------------- | ------------------------------------- | ------------- | -------- | ----------------------------------------------- |
| Valid user login                        | TC_LOGIN_001        | Login            | High                | tests/test_login.py                | LoginPage, HomePage                   | Yes           | Selected | Core authentication flow.                       |
| Invalid password login                  | TC_LOGIN_002        | Login            | High                | tests/test_login.py                | LoginPage                             | Yes           | Selected | Negative login case with clear error assertion. |
| Empty username validation               | TC_LOGIN_003        | Login            | Medium              | tests/test_login.py                | LoginPage                             | No            | Selected | Simple required-field validation.               |
| Successful logout                       | TC_LOGOUT_001       | Logout           | High                | tests/test_login.py                | LoginPage, HomePage                   | Yes           | Selected | Basic session ending flow.                      |
| Search patient by valid name            | TC_SEARCH_001       | Patient Search   | High                | tests/test_patient_search.py       | HomePage, PatientSearchPage           | Yes           | Selected | Important patient search flow.                  |
| Search with non-existing keyword        | TC_SEARCH_003       | Patient Search   | Medium              | tests/test_patient_search.py       | PatientSearchPage                     | Yes           | Selected | Negative search case.                           |
| Open patient profile from search result | TC_PROFILE_001      | Patient Profile  | High                | tests/test_patient_search.py       | PatientSearchPage, PatientSearchPage / Patient Dashboard | Yes           | Selected | Connects search result with patient profile.    |
| Missing given name validation           | TC_REGISTER_002     | Register Patient | High                | tests/test_patient_registration.py | HomePage, PatientRegistrationPage     | Optional      | Selected | Important form validation case.                 |

## 4. Deferred / Optional Automation Cases

The following test cases are not included in the first automation scope. They may be automated later after the basic framework is stable.

| Manual Test Case ID | Module           | Reason for Deferring                                                                |
| ------------------- | ---------------- | ----------------------------------------------------------------------------------- |
| TC_LOGIN_004        | Login            | Similar to TC_LOGIN_003; can be added later.                                        |
| TC_LOGIN_005        | Login            | Location behavior may vary depending on demo configuration.                         |
| TC_LOGIN_006        | Login            | Similar to invalid password test.                                                   |
| TC_LOGOUT_002       | Logout           | More security-related and may require stable URL/session handling.                  |
| TC_SEARCH_002       | Patient Search   | Depends on stable patient identifier data.                                          |
| TC_SEARCH_004       | Patient Search   | Empty search behavior may vary by implementation.                                   |
| TC_SEARCH_005       | Patient Search   | Special character behavior is useful but lower priority for first automation scope. |
| TC_PROFILE_002      | Patient Profile  | Can be automated after profile page object is stable.                               |
| TC_PROFILE_003      | Patient Profile  | Depends on available demo patient demographic data.                                 |
| TC_REGISTER_001     | Register Patient | Creates new data on public demo; better to run on local/stable environment.         |
| TC_REGISTER_003     | Register Patient | Similar validation group; can be added after TC_REGISTER_002.                       |
| TC_REGISTER_004     | Register Patient | Similar validation group; can be added after TC_REGISTER_002.                       |
| TC_REGISTER_005     | Register Patient | Invalid birthdate behavior depends on UI control.                                   |
| TC_REGISTER_006     | Register Patient | Confirmation page automation can be added after valid registration flow is stable.  |
| TC_REGISTER_007     | Register Patient | Cancel/exit behavior is more suitable for manual usability testing.                 |
| TC_REGISTER_008     | Register Patient | Phone field may be optional depending on demo configuration.                        |

## 5. Planned Selenium Test Structure

```text
selenium-ui-automation/
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   ├── patient_search_page.py
│   ├── patient_profile_page.py
│   └── patient_registration_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_patient_search.py
│   └── test_patient_registration.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

## 6. Planned Automation Test Mapping

| Selenium Test File                 | Test Function                                       | Related Manual Test Case |
| ---------------------------------- | --------------------------------------------------- | ------------------------ |
| tests/test_login.py                | test_login_with_valid_credentials                   | TC_LOGIN_001             |
| tests/test_login.py                | test_login_with_invalid_password                    | TC_LOGIN_002             |
| tests/test_login.py                | test_login_with_empty_username                      | TC_LOGIN_003             |
| tests/test_login.py                | test_logout_successfully                            | TC_LOGOUT_001            |
| tests/test_patient_search.py       | test_search_patient_by_valid_name                   | TC_SEARCH_001            |
| tests/test_patient_search.py       | test_search_patient_with_non_existing_keyword       | TC_SEARCH_003            |
| tests/test_patient_search.py       | test_open_patient_profile_from_search_result        | TC_PROFILE_001           |
| tests/test_patient_registration.py | test_required_validation_when_given_name_is_missing | TC_REGISTER_002          |

## 7. Conclusion

For the first Selenium automation scope, 8 manual test cases are selected.

These selected cases cover the most important regression flows:

* Login
* Logout
* Patient search
* Patient profile access
* Patient registration validation

Other manual test cases are kept as deferred or optional automation candidates because they may depend on unstable demo data, changing UI behavior, or lower-priority usability checks.
