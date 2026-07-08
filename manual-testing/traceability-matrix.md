# Traceability Matrix

## 1. Overview

This traceability matrix maps manual test coverage to implemented Selenium UI automation and Postman API testing.

The purpose of this document is to show which manual test cases are automated, which are API-backed, and which are intentionally deferred because they depend on public demo data, shared-environment behavior, or data creation.

Automation is not applied to every manual test case. Only stable, repeatable, high-priority, and easy-to-assert test cases are selected for the first automation scope.

## 2. Automation Selection Criteria

| Criteria | Description |
|---|---|
| High business value | The test case covers an important user flow. |
| Repeatable | The test case is useful for regression testing. |
| Stable UI flow | The page and elements are reasonably stable. |
| Clear expected result | The result can be verified by assertion. |
| Low dependency on changing demo data | The test does not depend heavily on unstable public demo data. |
| Safe for shared demo | The test does not create unnecessary records in the public O2 demo. |

## 3. Implemented Selenium Automation Scope

| Requirement / Flow | Related Manual Test Case ID | Module | Selenium Test File | Test Function | Status | Notes |
|---|---|---|---|---|---|---|
| O2 login page loads | Smoke / environment check | Login | `tests/test_o2_login_page.py` | `test_o2_login_page_loads` | Implemented | Confirms the login page and location list are visible. |
| Valid user login | `TC_LOGIN_001` | Login | `tests/test_login.py` | `test_login_with_valid_credentials` | Implemented | Core authentication flow. |
| Invalid password login | `TC_LOGIN_002` | Login | `tests/test_login.py` | `test_login_with_invalid_password_shows_error` | Implemented | Negative login case with error assertion. |
| Successful logout | `TC_LOGOUT_001` | Logout | `tests/test_login.py` | `test_logout_returns_user_to_login_page` | Implemented | Confirms session end and return to login page. |
| Search patient by common keyword | `TC_SEARCH_001` | Patient Search | `tests/test_patient_search.py` | `test_search_patient_by_common_keyword_shows_results` | Implemented / data-dependent | Uses `OPENMRS_PATIENT_SEARCH`; skips honestly if public demo data returns no rows. |
| Open first patient profile from search result | `TC_PROFILE_001` | Patient Profile | `tests/test_patient_search.py` | `test_open_first_patient_profile_from_search_results` | Implemented / data-dependent | Runs only when search result exists. |
| Search with non-existing keyword | `TC_SEARCH_003` | Patient Search | `tests/test_patient_search.py` | `test_search_patient_with_unlikely_keyword_shows_no_matching_records` | Implemented | Negative search case with stable assertion. |
| Register patient page opens | Registration smoke check | Register Patient | `tests/test_patient_registration.py` | `test_register_patient_page_opens` | Optional | Disabled by default to avoid shared-demo data pollution. |
| Registration name step accepts dummy data when Next is available | Registration safe wizard check | Register Patient | `tests/test_patient_registration.py` | `test_register_patient_name_step_accepts_dummy_data_when_next_is_available` | Optional | Does not claim full patient registration; checks page/name-step progression only. |

## 4. Deferred / Optional Manual Test Cases

The following test cases are designed in the manual workbook but are not part of the stable default Selenium suite.

| Manual Test Case ID | Module | Current Decision | Reason |
|---|---|---|---|
| `TC_LOGIN_003` | Login | Deferred | Empty username validation is documented but not implemented in current Selenium code. |
| `TC_LOGIN_004` | Login | Deferred | Similar required-field validation; can be added later. |
| `TC_LOGIN_005` | Login | Deferred | Location behavior may vary depending on demo configuration. |
| `TC_LOGIN_006` | Login | Deferred | Similar to invalid password test; lower value for first automation scope. |
| `TC_LOGOUT_002` | Logout | Deferred | Requires stable protected URL/session behavior. |
| `TC_SEARCH_002` | Patient Search | Deferred / blocked | Depends on stable patient identifier data. |
| `TC_SEARCH_004` | Patient Search | Deferred | Empty search behavior may vary by implementation. |
| `TC_SEARCH_005` | Patient Search | Deferred | Special character behavior is useful but lower priority for first automation scope. |
| `TC_SEARCH_006` | Patient Search | Deferred | Requires two stable demo keywords. |
| `TC_PROFILE_002` | Patient Profile | Deferred / data-dependent | Depends on available patient result and stable profile layout. |
| `TC_PROFILE_003` | Patient Profile | Deferred / data-dependent | Depends on available demographic data. |
| `TC_PROFILE_004` | Patient Profile | Deferred | Navigation behavior is better checked manually first. |
| `TC_REGISTER_001` | Register Patient | Optional / local only | Full registration creates data; should be run on a local/stable environment. |
| `TC_REGISTER_002` | Register Patient | Deferred | Missing given-name validation is not implemented in current Selenium code. |
| `TC_REGISTER_003` | Register Patient | Deferred | Missing family-name validation can be added later. |
| `TC_REGISTER_004` | Register Patient | Deferred | Missing gender validation depends on wizard step behavior. |
| `TC_REGISTER_005` | Register Patient | Deferred | Invalid birthdate behavior depends on UI controls. |
| `TC_REGISTER_006` | Register Patient | Deferred | Confirmation page check requires full registration flow. |
| `TC_REGISTER_007` | Register Patient | Manual first | Cancel/exit behavior is more suitable for manual usability testing. |
| `TC_REGISTER_008` | Register Patient | Deferred | Phone field may be optional depending on demo configuration. |

## 5. Implemented Selenium Test Structure

```text
selenium-ui-automation/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── patient_search_page.py
│   └── patient_registration_page.py
├── tests/
│   ├── test_o2_login_page.py
│   ├── test_login.py
│   ├── test_patient_search.py
│   └── test_patient_registration.py
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
└── README.md
```

## 6. API Traceability Summary

| API Area | Postman Request | Related UI / Manual Coverage | Notes |
|---|---|---|---|
| Authentication/session | `API_AUTH_001`, `API_AUTH_002` | Login positive/negative | Public demo session behavior may vary. |
| User search | `API_USER_001` | Login/user context | Validates user lookup response structure. |
| Location search | `API_LOCATION_001` | Login location selection | Confirms configured login location exists. |
| Patient search | `API_PATIENT_001` | Patient search | Saves first patient UUID when data exists. |
| Patient detail | `API_PATIENT_002` | Patient profile | Uses dynamic UUID or controlled fallback. |
| Invalid UUID | `API_NEG_001` | Negative API behavior | `500` is recorded as robustness observation, not ideal product pass. |
| No-auth patient search | `API_OBS_002` | Basic access-control observation | `200` is recorded as public-demo access-control/configuration observation. |

## 7. Conclusion

The current Selenium suite implements stable login, logout, patient search, patient-profile navigation, and optional registration smoke checks. Empty username validation and missing given-name validation remain documented as manual/future coverage rather than implemented Selenium automation.

This keeps the traceability matrix aligned with the actual implementation and available evidence.
