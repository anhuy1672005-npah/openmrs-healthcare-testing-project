# Postman API Testing - OpenMRS O2

This folder contains the Postman API testing assets for the OpenMRS Healthcare Web Testing Project.

## Target system

```text
OpenMRS O2 / Reference Application 2.x
App URL: https://o2.openmrs.org/openmrs
REST API base URL: https://o2.openmrs.org/openmrs/ws/rest/v1
```

The public O2 demo uses demo credentials and shared demo data only. Do not use real patient data.

## Files

```text
postman-api-testing/
├── openmrs-api-collection.json
├── openmrs-environment.json
├── api-test-cases.md
├── api-test-summary.md
└── README.md
```

## How to run in Postman

1. Open Postman.
2. Import `openmrs-api-collection.json`.
3. Import `openmrs-environment.json`.
4. Select environment: `OpenMRS O2 Demo Environment`.
5. Open Collection Runner.
6. Turn off `Stop run if an error occurs`.
7. Turn on `Run collection without using stored cookies`.
8. Run collection: `OpenMRS O2 REST API Testing Collection`.
9. Export/save the run result into `evidence/api-report/`.

## Runner settings

| Setting | Value |
|---|---|
| Environment | `OpenMRS O2 Demo Environment` |
| Iterations | `1` |
| Stop run if an error occurs | Off |
| Run collection without using stored cookies | On |
| Keep variable values | On |

## Testing strategy

The API scope focuses on safe and repeatable requests:

- Valid authentication/session check
- Invalid authentication check
- User search
- Location search with configured login-location match assertion
- Patient search
- Patient detail retrieval when a search result exists
- Invalid UUID negative/robustness test
- No-auth patient search observation

Create/update/delete patient API requests are not included in the default collection because the public O2 demo is shared and should not be polluted with unnecessary test data.

## Public demo behavior

The O2 public demo can return behavior that would be considered imperfect in a stricter API environment. The collection records these as QA observations rather than hiding them:

- Valid `/session` may return `500`.
- Invalid patient UUID may return `500` instead of `400` or `404`.
- No-auth patient search may return `200` depending on public demo configuration.

These are useful points to mention in the final test summary as environment limitations or QA recommendations.

## How to run from command line with Newman optional

Install Newman if needed:

```bash
npm install -g newman
```

Run collection:

```bash
newman run postman-api-testing/openmrs-api-collection.json \
  -e postman-api-testing/openmrs-environment.json \
  --reporters cli,json \
  --reporter-json-export evidence/api-report/openmrs-o2-api-report.json
```

## Public O2 authentication note

The invalid-password session request is treated as a behavior-observation test. In a Postman collection run, OpenMRS O2 may reuse an active session cookie created by another request. For that reason, the invalid-password request accepts and documents several possible public-demo behaviors: `401/403`, `500`, `200 authenticated=false`, or `200 authenticated=true` when a session cookie is reused.

For the cleanest auth isolation, run the collection with:

- `Run collection without using stored cookies`: ON
- `Stop run if an error occurs`: OFF
- `Keep variable values`: ON

