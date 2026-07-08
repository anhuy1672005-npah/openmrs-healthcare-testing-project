# API Test Cases

## 1. API Testing Scope

The API testing scope focuses on safe and repeatable OpenMRS O2 REST API requests. The collection validates authentication/session behavior, user search, location lookup, patient search, patient detail retrieval when data is available, invalid UUID handling, and no-auth access behavior.

Create, update, and delete requests are intentionally excluded from the default collection because the public OpenMRS O2 demo is shared and should not be polluted with unnecessary test data.

## 2. Test Data and Environment Variables

| Variable | Example Value | Purpose |
|---|---|---|
| `base_url` | `https://o2.openmrs.org/openmrs/ws/rest/v1` | OpenMRS REST API base URL |
| `username` | `admin` | Demo API username |
| `password` | `Admin123` | Demo API password |
| `invalid_password` | `WrongPassword123` | Negative authentication testing |
| `openmrs_location` | `Registration Desk` | Location lookup and UI/API mapping |
| `patient_search_keyword` | `a` | Patient search keyword; can be changed if demo data changes |
| `invalid_uuid` | `00000000-0000-0000-0000-000000000000` | Negative UUID testing |
| `patient_uuid` | Dynamic | Saved from `API_PATIENT_001` when search returns at least one patient |
| `auth_session_observation` | Dynamic | Captures `/session` behavior in the public demo |
| `invalid_uuid_observation` | Dynamic | Captures invalid UUID behavior |
| `no_auth_patient_search_observation` | Dynamic | Captures no-auth patient search behavior |

## 3. API Test Case Table

| API Case ID | Request Name | Feature | Method | Endpoint | Test Type | Main Assertions | Related Manual / Selenium Flow | Expected Result | Default Status |
|---|---|---|---|---|---|---|---|---|---|
| API_AUTH_001 | Get Session with Valid Credentials | Authentication | GET | `/session` | Positive / public-demo-aware | Status `200` with JSON and `authenticated=true`; if public demo returns `500`, document environment/server observation | TC_LOGIN_001 / login valid | Authenticated session is returned, or demo limitation is documented | Automated in Postman |
| API_AUTH_002 | Get Session with Invalid Password | Authentication | GET | `/session` | Negative / public-demo-aware | Status `401/403`, or `200` with `authenticated=false`; `500` is documented if public demo returns server error | TC_LOGIN_002 / login invalid | Invalid credentials are rejected or unauthenticated | Automated in Postman |
| API_USER_001 | Search User by Username | User | GET | `/user?q={{username}}&v=default` | Positive | Status `200`, JSON response, `results` array | Login/API user context | User search response structure is valid | Automated in Postman |
| API_LOCATION_001 | Search Login Location by Name | Location | GET | `/location?q={{openmrs_location}}&v=default` | Positive | Status `200`, JSON response, `results` array | Location selection at login | Location lookup response structure is valid | Automated in Postman |
| API_PATIENT_001 | Search Patient by Keyword | Patient Search | GET | `/patient?q={{patient_search_keyword}}&v=default` | Positive / data-dependent | Status `200`, JSON response, `results` array; save first patient UUID when present | TC_SEARCH_001 / patient search | Search endpoint returns valid structure | Automated in Postman |
| API_PATIENT_002 | Get Patient Detail by UUID from Search Result | Patient Detail | GET | `/patient/{{effective_patient_uuid}}?v=full` | Positive / controlled fallback | If patient UUID exists: status `200` and UUID matches. If not: controlled `400/404/500` fallback | TC_PROFILE_001 / open patient profile | Patient detail is returned when search data exists; otherwise fallback is documented | Automated in Postman |
| API_NEG_001 | Get Patient with Invalid UUID | Patient Detail | GET | `/patient/{{invalid_uuid}}?v=default` | Negative / robustness | Status `400/404`; public demo may return `500`, which is documented as backend robustness observation | Invalid data / negative API test | Invalid UUID does not return valid patient data | Automated in Postman |
| API_OBS_002 | No-auth Patient Search Behavior | Security / Authorization | GET | `/patient?q={{patient_search_keyword}}&v=default` | Access-control observation | Status `401/403`; public demo may return `200`, which is documented as access-control/configuration observation | Access control check | Request without valid authentication should be rejected in strict environments | Automated in Postman |

## 4. Notes

- `API_PATIENT_002` is designed to run after `API_PATIENT_001` in the Collection Runner.
- If `API_PATIENT_001` does not return patient data because public demo data changed, `API_PATIENT_002` falls back to an invalid UUID and validates the not-found/error behavior instead of failing the whole collection for unstable demo data.
- To make patient detail testing strictly positive, manually update `patient_search_keyword` to a keyword that returns patient records in the current O2 demo environment.
- If `/session`, invalid UUID, or no-auth patient search returns behavior that is not ideal, document it in `api-test-summary.md` as a public demo limitation or QA recommendation rather than deleting the evidence.
