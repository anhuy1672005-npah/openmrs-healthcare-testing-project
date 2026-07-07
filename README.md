# OpenMRS Healthcare Web Testing Project

## Overview

This project demonstrates an end-to-end QA workflow for **OpenMRS O2 / Reference Application 2.x**.

It includes:

- Manual Testing
- Selenium UI Automation with Python, Selenium WebDriver, and Pytest
- Postman REST API Testing
- Traceability mapping between manual, automation, and API coverage
- QA observations and test summary documentation

The project focuses on key healthcare workflows such as login, logout, patient search, patient profile viewing, patient registration validation, and selected REST API checks.

## Target Application

```text
Application: OpenMRS O2 / Reference Application 2.x
App URL: https://o2.openmrs.org/openmrs
REST API: https://o2.openmrs.org/openmrs/ws/rest/v1
Demo user: admin / Admin123
Default location: Registration Desk
```

Only demo/dummy data is used. Do not use real patient data.

## Project Structure

```text
openmrs-healthcare-testing-project-main/
├── README.md
├── project-overview.md
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
    ├── manual-screenshots/
    ├── automation-report/
    ├── api-report/
    └── bug-evidence/
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

Generate HTML report:

```powershell
pytest -m "not registration" --html=..\evidence\automation-report\selenium-report.html --self-contained-html
```

Optional registration tests:

```powershell
$env:RUN_REGISTRATION_TESTS="true"
pytest -m registration -v
```

Registration tests are optional because the public O2 demo is shared and may create dummy patient records.

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
- Invalid UUID behavior
- No-auth patient search observation

## Evidence

Do not upload fake evidence. Store only real execution outputs:

- Manual screenshots: `evidence/manual-screenshots/`
- Pytest HTML reports: `evidence/automation-report/`
- Postman run exports: `evidence/api-report/`
- Bug/observation screenshots: `evidence/bug-evidence/`

## Notes for Reviewers

This is a QA portfolio project, not a production test suite. Because the public OpenMRS O2 demo is shared, some tests intentionally skip or document behavior instead of failing on unstable external data.
