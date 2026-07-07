# Test Summary Report

## 1. Test Scope

This report summarizes QA activities for the OpenMRS O2 Healthcare Web Testing Project.

Scope covered:

- Manual testing for core OpenMRS O2 workflows
- Selenium UI automation for stable regression flows
- Postman API testing for REST API behavior
- QA observations and environment limitations

Out of scope:

- Real patient data
- Database testing
- Performance testing
- Security testing beyond basic unauthorized/no-auth API checks
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
| Manual test cases planned/executed | 28 |
| Critical defects found | 0 |
| QA observations/recommendations | 5 |

Detailed test cases are stored in `manual-testing/test_cases.xlsx`.

Since no critical functional defect was identified, this project documents real observations and recommendations instead of fabricating bugs. See:

```text
manual-testing/observed-issues-and-recommendations.md
```

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
| Location resource | Search login location |
| Patient resource | Search patient and retrieve patient detail when UUID exists |
| Negative cases | Invalid UUID and no-auth patient search behavior |

Public O2 API behavior may vary because the demo is shared. The collection documents these as QA observations instead of hiding them.

## 6. Defects / Observed Issues

| Type | Count |
|---|---:|
| Critical functional defects | 0 |
| Usability improvements | 1 |
| Validation improvements | 1 |
| QA documentation improvements | 1 |
| Test environment risks | 2 |
| Total observations / recommendations | 5 |

## 7. Risks and Limitations

| Risk | Impact | Mitigation |
|---|---|---|
| Public demo data can change | Patient search/profile tests may skip or behave differently | Use skip logic and document environment dependency |
| O2 demo API may return non-strict behavior | Some endpoints may return 500 or 200 where stricter APIs would return 400/401/404 | Document behavior in API summary |
| Registration creates data on public demo | Test data pollution | Keep registration tests optional |
| Screenshots/reports must be generated locally | Evidence can become outdated | Store real execution reports in `evidence/` after each run |

## 8. Conclusion

The project demonstrates a complete QA workflow: manual testing defines coverage, Selenium automates stable UI regression flows, Postman validates API behavior, and traceability connects the layers.

The project is suitable as a QA portfolio project once real execution evidence is added to the `evidence/` folders.
