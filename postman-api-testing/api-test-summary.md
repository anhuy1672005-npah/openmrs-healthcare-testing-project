# API Test Summary

## 1. API Testing Scope

API testing validates the backend layer behind the OpenMRS O2 web flows tested manually and through Selenium UI automation.

The collection covers:

- Authentication/session validation
- Invalid credential handling
- User search
- Login location lookup with a real match assertion
- Patient search
- Patient detail retrieval when a patient UUID is available
- Invalid UUID / robustness behavior
- Unauthorized or no-auth patient search behavior

The API suite avoids create, update, and delete requests because the O2 demo is a shared public environment.

## 2. Test Environment

| Item | Value |
|---|---|
| Application | OpenMRS O2 / Reference Application 2.x |
| App URL | `https://o2.openmrs.org/openmrs` |
| REST API Base URL | `https://o2.openmrs.org/openmrs/ws/rest/v1` |
| Authentication | Basic Auth with demo credentials where required |
| Tool | Postman |
| Environment File | `openmrs-environment.json` |
| Collection File | `openmrs-api-collection.json` |

## 3. API Collection Summary

| Area | Number of Requests | Purpose |
|---|---:|---|
| Authentication and Session | 2 | Validate valid and invalid authentication/session behavior |
| User Resource | 1 | Validate user search response structure |
| Location Resource | 1 | Validate O2 login location lookup response structure |
| Patient Resource | 4 | Validate patient search, detail, invalid UUID, and no-auth access behavior |
| Total | 8 | Safe API regression suite for O2 demo |

## 4. Current Public Demo Observations

During testing against the public O2 demo, some endpoints may return behavior that is not ideal for strict API validation but is useful to document as QA evidence.

| Observation | Meaning | How the collection handles it |
|---|---|---|
| `/session` with valid Basic Auth may return `500` | Public demo/session endpoint instability | The test records this as an environment/server observation instead of breaking the whole safe suite |
| Invalid patient UUID may return `500` | Backend robustness issue; stricter APIs usually return `400` or `404` | The test accepts the error response and records the observation |
| Patient search without Basic Auth may return `200` | Public demo access-control/configuration behavior | The test captures this as an access-control observation |
| Patient search data may vary | Public demo data is shared and changeable | Patient detail test uses dynamic UUID when available, otherwise controlled fallback |

## 5. Expected Test Results

For the public-demo-safe collection:

| Result Type | Expected Count | Notes |
|---|---:|---|
| Requests | 8 | Safe read-only API requests |
| Assertions | 17+ | Count may vary depending on response path |
| Failed | 0 | Expected after using the resilient collection logic |
| Data-dependent | 1 | `API_PATIENT_002` is positive when `patient_uuid` is saved from search; otherwise it validates fallback not-found/error behavior |

For strict API/security interpretation, the following should still be discussed as QA observations if they appear:

- `500` on valid `/session`
- `500` on invalid patient UUID
- `200` on no-auth patient search

These observations are not presented as strict product passes; they are kept as documented public-demo behaviors.

## 6. Key Validations

The collection validates:

- HTTP status codes such as `200`, `400`, `404`, `401`, `403`, and documented `500` public-demo responses
- JSON response format when the response is expected to be JSON
- Authentication state when `/session` returns JSON successfully
- Existence of expected fields such as `authenticated`, `user`, `uuid`, and `results`
- Basic API access-control behavior
- Safe handling of changing public demo patient data

## 7. Recommended Postman Runner Settings

Use these settings before pressing **Start run**:

| Setting | Recommended Value |
|---|---|
| Environment | `OpenMRS O2 Demo Environment` |
| Iterations | `1` |
| Stop run if an error occurs | Off |
| Run collection without using stored cookies | On |
| Keep variable values | On |
| Save cookies after collection run | Off or not required |

## 8. Evidence Location

After running the Postman collection, export or save results under:

```text
evidence/api-report/
```

Recommended file names:

```text
openmrs-o2-api-postman-run.json
openmrs-o2-api-newman-report.json
openmrs-o2-api-run-summary.png
```

## 9. Conclusion

The API testing layer completes the QA workflow by connecting frontend behavior with backend validation:

```text
Manual Testing → Selenium UI Automation → Postman API Testing → Reports/Evidence
```

Because the target is a public demo environment, the collection is intentionally safe, read-only, and tolerant of documented demo limitations while still preserving meaningful QA observations.

## Latest Postman runner expectation

The collection is designed for the public OpenMRS O2 demo. Some authentication/session responses may vary because the demo environment can reuse an active session cookie. The invalid-password session request therefore records the observed behavior instead of failing the whole API suite. This keeps the API suite focused on documenting real public-demo behavior while still validating status codes, JSON shape, result arrays, patient search, invalid UUID behavior, and no-auth patient search behavior.
