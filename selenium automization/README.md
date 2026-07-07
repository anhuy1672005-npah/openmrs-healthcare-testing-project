# Selenium UI Automation - OpenMRS O2 / Reference Application 2.x

This Selenium suite is written for **OpenMRS O2**, not OpenMRS O3.

Default application URL:

```text
https://o2.openmrs.org/openmrs
```

Default demo credentials:

```text
Username: admin
Password: Admin123
Location: Registration Desk
```

OpenMRS O2 login is location-based. The login page contains locations such as
`Inpatient Ward`, `Isolation Ward`, `Laboratory`, `Outpatient Clinic`,
`Pharmacy`, and `Registration Desk`.

## Why this suite is structured this way

The project follows a QA workflow:

1. Manual test cases define important business flows.
2. Traceability matrix maps manual cases to automation candidates.
3. Selenium automates stable regression flows.
4. Registration tests are coded but disabled by default because creating data on a public demo can make tests unstable and noisy.

## Automated flows

Stable by default:

- Open O2 login page
- Login with valid credentials
- Login with invalid password
- Logout
- Find Patient Record
- Open first patient profile from search results
- Search with unlikely keyword and verify no matching records

Optional:

- Register patient page opens
- Fill required name step with dummy data

## Setup on Windows PowerShell

From the project root:

```powershell
cd .\selenium-ui-automation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

If PowerShell blocks venv activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Recommended commands

Run smoke/login tests first:

```powershell
pytest tests/test_o2_login_page.py tests/test_login.py -v
```

Run stable tests but skip registration:

```powershell
pytest -m "not registration"
```

Run with HTML report:

```powershell
pytest -m "not registration" --html=..\evidence\automation-report\selenium-report.html --self-contained-html
```

Enable registration tests only when you really want to create demo data:

```powershell
$env:RUN_REGISTRATION_TESTS="true"
pytest -m registration
```

## Local configuration

Copy `.env.example` to `.env` if you need to change URL, credentials, location,
search keyword, or browser mode.

```powershell
copy .env.example .env
```

Common variables:

```text
OPENMRS_BASE_URL=https://o2.openmrs.org/openmrs
OPENMRS_USERNAME=admin
OPENMRS_PASSWORD=Admin123
OPENMRS_LOCATION=Registration Desk
OPENMRS_PATIENT_SEARCH=John
HEADLESS=false
RUN_REGISTRATION_TESTS=false
```

## Notes

Because the public O2 demo data can change, patient search tests skip themselves
when the configured keyword returns no patients. This is intentional: it keeps the
test result honest instead of pretending that unstable external demo data is a
product defect.

## Registration test behavior

Registration tests are implemented but optional because the public OpenMRS O2 demo is shared and the registration wizard may create dummy patient data.

Run the stable suite first:

```powershell
pytest -m "not registration"
```

Run registration only when you intentionally want to verify the registration page/first-step flow:

```powershell
$env:RUN_REGISTRATION_TESTS="true"
pytest -m registration
```

If the public demo does not expose an enabled **Next** button after dummy name entry, the second registration test is skipped instead of failed. This is intentional to avoid false failures caused by shared demo environment differences.

