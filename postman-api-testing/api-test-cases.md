# API Test Cases

| API Case ID | Feature | Method | Test Type | Expected Result | Status |
|---|---|---|---|---|---|
| API_AUTH_001 | Session / Authentication | GET | Positive | Status code 200 and session information is returned | Planned |
| API_USER_001 | Get current user | GET | Positive | Current user information is returned | Planned |
| API_PATIENT_001 | Search patient/person | GET | Positive | Search results are returned | Planned |
| API_PATIENT_002 | Get patient/person by UUID | GET | Positive | Patient/person details are returned | Planned |
| API_NEG_001 | Invalid UUID | GET | Negative | Error response is returned | Planned |
| API_NEG_002 | Unauthorized request | GET | Negative | Unauthorized error is returned | Planned |
| API_NEG_003 | Missing or invalid parameter | GET/POST | Negative | Validation or error response is returned | Planned |
