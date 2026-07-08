# Test Summary Report

## 1. Test Scope

This report summarizes QA activities for the OpenMRS O2 Healthcare Web Testing Project.

Scope covered:

- Manual test design for core OpenMRS O2 workflows
- Evidence-based manual execution tracking in Excel
- Selenium UI automation for stable regression flows
- Postman API testing for REST API behavior
- QA observations and environment limitations

Out of scope:

- Real patient data
- Database testing
- Performance testing
- Advanced security testing beyond basic no-auth API observation
- Full patient-registration submission on the shared public demo
- Production-level CI/CD

## 2. Test Environment

| Item | Value |
|---|---|
| Application | OpenMRS O2 / Reference Application 2.x |
| App URL | `https://o2.openmrs.org/openmrs` |
| API Base URL | `https://o2.openmrs.org/openmrs/ws/rest/v1` |
| Browser | Google Chrome |
| UI Automation | Python, Selenium WebDriver, Pytest |
| API Testing | Postman |
| Test Data | Public demo data and dummy data only |

## 3. Manual Testing Summary

| Item | Result |
|---|---:|
| Test scenarios documented | 24 |
| Manual test cases designed | 28 |
| Evidence-backed manual/API/UI pass entries in workbook | 6 |
| Failed | 0 |
| Blocked / data-dependent | 5 |
| Skipped / optional public-demo registration cases | 8 |
| Not run | 9 |
| QA observations/recommendations | 7 |

Detailed test cases are stored in:

```text
manual-testing/test_cases.xlsx
```

Execution note: cases without direct evidence or stable demo data are marked as `Not Run`, `Blocked`, or `Skipped` instead of being counted as passed.

## 4. Selenium Automation Summary

Stable suite command:

```powershell
cd selenium-ui-automation
pytest -m "not registration" --html=../evidence/automation-report/selenium-report.html --self-contained-html
```

Core automated flows:

- Open O2 login page
- Login with valid credentials
- Login with invalid password
- Logout
- Patient search with available demo data
- Open patient profile when search results exist
- Negative patient search with unlikely keyword

The configured default patient search keyword was changed from `John` to `a` to reduce the chance of skipped positive search/profile tests on the public demo. Because demo data can still change, these tests keep skip logic and document the reason when no rows are returned.

Registration tests are implemented but optional because the O2 demo is shared and registration may create dummy patient data.

Optional registration command:

```powershell
$env:RUN_REGISTRATION_TESTS="true"
pytest -m registration -v
```

## 5. API Testing Summary

Postman files:

```text
postman-api-testing/openmrs-api-collection.json
postman-api-testing/openmrs-environment.json
```

API areas covered:

| Area | Coverage |
|---|---|
| Authentication/session | Valid and invalid session behavior |
| User resource | Search user by username |
| Location resource | Search configured login location |
| Patient resource | Search patient and retrieve patient detail when UUID exists |
| Negative/observation cases | Invalid UUID and no-auth patient search behavior |

The Postman collection can pass technically while still documenting non-ideal public-demo behavior. In the report, `500` for invalid UUID and `200` for no-auth patient search are treated as QA observations, not as strict product success criteria.

## 6. Defects / Observed Issues

| Type | Count |
|---|---:|
| Critical functional defects | 0 |
| Usability improvements | 1 |
| Validation improvements | 1 |
| QA documentation improvements | 1 |
| Test environment risks | 2 |
| API robustness/access-control observations | 2 |
| Total observations / recommendations | 7 |

## 7. Risks and Limitations

| Risk | Impact | Mitigation |
|---|---|---|
| Public demo data can change | Patient search/profile tests may skip or behave differently | Use common keyword `a`, keep skip logic, and document environment dependency |
| O2 demo API may return non-strict behavior | Some endpoints may return `500` or `200` where stricter APIs would return `400/401/404` | Document behavior in API summary and observed issues |
| Registration creates data on public demo | Test data pollution | Keep registration tests optional |
| Screenshots/reports must be regenerated locally | Evidence can become outdated after code changes | Rerun Selenium/Postman and store real execution reports in `evidence/` |

## 8. Conclusion

The project demonstrates a complete QA workflow: manual test design defines coverage, Selenium automates stable UI regression flows, Postman validates API behavior, and traceability connects the layers.

The project keeps the scope small and evidence-based. It demonstrates basic QA thinking, automation structure, API validation, and clear reporting without overstating coverage.
