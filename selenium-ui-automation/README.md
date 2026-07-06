# Selenium UI Automation

This folder contains Selenium UI automation tests for the OpenMRS Healthcare Web Testing Project.

## Tools

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Chrome / ChromeDriver

## Test Areas

- Login
- Logout
- Patient search
- Patient profile
- Patient registration
- Form validation

## Folder Structure

selenium-ui-automation/
- pages/
  - login_page.py
  - home_page.py
  - patient_search_page.py
  - patient_registration_page.py
- tests/
  - test_login.py
  - test_patient_search.py
  - test_patient_registration.py
- conftest.py
- requirements.txt
- README.md

## How to Install Dependencies

Run this command inside the selenium-ui-automation folder:

pip install -r requirements.txt

## How to Run Tests

Run:

pytest

## How to Generate HTML Report

Run:

pytest --html=../evidence/automation-report/report.html
