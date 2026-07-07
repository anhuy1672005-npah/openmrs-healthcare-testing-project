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

OpenMRS O2 login is location-based. The login page contains locations such as `Inpatient Ward`, `Isolation Ward`, `Laboratory`, `Outpatient Clinic`, `Pharmacy`, and `Registration Desk`.

## Automated flows

Stable by default:

- Open O2 login page
- Login with valid credentials
- Login with invalid password
- Logout
- Find Patient Record
- Open first patient profile from search results when demo data is available
- Search with unlikely keyword and verify no matching records

Optional:

- Register patient page opens
- Fill required name step with dummy data when the O2 wizard exposes an enabled Next button

Registration tests are optional because the public O2 demo is shared and the wizard may create dummy patient data.

## Setup on Windows PowerShell

From the project root:

```powershell
cd .\selenium-ui-automation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks virtual environment activation:

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

Run stable tests with HTML report:

```powershell
pytest -m "not registration" --html=..\evidence\automation-report\selenium-report.html --self-contained-html
```

Run registration tests only when you intentionally want to verify the optional registration page/name-step flow:

```powershell
$env:RUN_REGISTRATION_TESTS="true"
pytest -m registration -v
```

## Local configuration

Copy `.env.example` to `.env` if you need to change URL, credentials, location, search keyword, or browser mode.

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

Because the public O2 demo data can change, patient search tests skip themselves when the configured keyword returns no patients. This is intentional: it keeps the test result honest instead of pretending that unstable external demo data is a product defect.

If the public demo does not expose an enabled **Next** button after dummy name entry, the second registration test is skipped instead of failed. This avoids false failures caused by shared demo environment differences.
