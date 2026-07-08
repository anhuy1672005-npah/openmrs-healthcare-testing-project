# OpenMRS Healthcare Web Testing Project

## Overview

This is a small QA portfolio project for the **OpenMRS O2 / Reference Application 2.x** public demo. It demonstrates a practical testing workflow using:

- Manual test design and execution tracking
- Selenium UI automation with Python, Selenium WebDriver, and Pytest
- Postman REST API testing
- Traceability between manual, UI automation, and API coverage
- Evidence-based test reporting

The project focuses on core flows: login, logout, patient search, patient profile viewing when demo data is available, safe registration-page checks, and selected read-only REST API checks.

## Target Application

```text
Application: OpenMRS O2 / Reference Application 2.x
App URL: https://o2.openmrs.org/openmrs
REST API: https://o2.openmrs.org/openmrs/ws/rest/v1
Demo user: admin / Admin123
Default location: Registration Desk
```

Only public demo data and dummy data are used. Real patient data is not used.

## Project Structure

```text
openmrs-healthcare-testing-project/
├── README.md
├── project-overview.md
├── LICENSE
├── .gitignore
├── manual-testing/
│   ├── application-map.md
│   ├── test-plan.md
│   ├── test-scenarios.md
│   ├── test-cases.md
│   ├── test_cases.xlsx
│   ├── traceability-matrix.md
│   ├── observed-issues-and-recommendations.md
│   └── test-summary-report.md
├── selenium-ui-automation/
│   ├── pages/
│   ├── tests/
│   ├── config.py
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
├── postman-api-testing/
│   ├── openmrs-api-collection.json
│   ├── openmrs-environment.json
│   ├── api-test-cases.md
│   ├── api-test-summary.md
│   └── README.md
└── evidence/
    ├── automation-report/
    ├── api-report/
    └── manual-screenshots/
```

## Manual Testing

Manual testing documents the business flows and expected behavior before automation.

Main files:

- `manual-testing/test-plan.md`
- `manual-testing/test-scenarios.md`
- `manual-testing/test_cases.xlsx`
- `manual-testing/traceability-matrix.md`
- `manual-testing/observed-issues-and-recommendations.md`
- `manual-testing/test-summary-report.md`

## Selenium UI Automation

From the project root:

```powershell
cd .\selenium-ui-automation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -m "not registration"
```

Generate an HTML report:

```powershell
pytest -m "not registration" --html=..\evidence\automation-report\selenium-report.html --self-contained-html
```

Optional registration checks:

```powershell
$env:RUN_REGISTRATION_TESTS="true"
pytest -m registration -v
```

Registration tests are optional because the public O2 demo is shared and may create dummy patient records. The optional Selenium registration tests check page access/name-step progression only; they do not claim full patient creation.

## Postman API Testing

Import into Postman:

```text
postman-api-testing/openmrs-api-collection.json
postman-api-testing/openmrs-environment.json
```

Runner settings:

```text
Environment: OpenMRS O2 Demo Environment
Iterations: 1
Stop run if an error occurs: OFF
Run collection without using stored cookies: ON
Keep variable values: ON
```

The API collection covers:

- Session/authentication behavior
- Invalid credential behavior
- User search
- Login location search
- Patient search
- Patient detail retrieval
- Invalid UUID robustness observation
- No-auth patient search access-control observation

## Evidence

Evidence files are stored under:

- Selenium report output path after running: `evidence/automation-report/selenium-report.html`
- Postman run screenshot: `evidence/api-report/openmrs-o2-api-run-summary.png`
- Optional manual screenshots: `evidence/manual-screenshots/`

After changing code or test data, regenerate the Selenium/Postman evidence from actual execution results.

## Notes for Reviewers

This is a QA portfolio project, not a production-level test suite. Because the OpenMRS O2 public demo is shared, some data-dependent checks may be skipped or documented as observations instead of being treated as product defects.
