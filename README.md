# OpenMRS Healthcare Web Testing Project

## Overview

This project demonstrates manual testing, Selenium UI automation, and Postman API testing for the OpenMRS healthcare web application demo.

The project focuses on key healthcare workflows such as login, patient search, patient profile viewing, patient registration, form validation, and selected REST API checks.

## Project Scope

### Manual Testing
- Test plan
- Test scenarios
- Manual test cases
- Test execution results
- Bug reports or QA recommendations
- Test summary report

### Selenium UI Automation
- Login tests
- Patient search tests
- Patient profile tests
- Patient registration tests
- Regression test execution with Pytest

### Postman API Testing
- Authentication/session checks
- Current user check
- Patient/person search
- Patient/person detail retrieval
- Negative API cases such as unauthorized request and invalid UUID

## Automation Scope

Based on the manual test cases, 8 high-priority test cases were selected for Selenium UI automation. These cases cover login, logout, patient search, patient profile access, and patient registration validation.

The full mapping between manual test cases and planned automation scripts is documented in:

manual-testing/traceability-matrix.md

## Tools Used

| Area | Tools |
|---|---|
| Manual Testing | Google Sheets / Excel, Markdown |
| UI Automation | Python, Selenium WebDriver, Pytest |
| API Testing | Postman |
| Bug Tracking | GitHub Issues / Markdown |
| Version Control | Git, GitHub |
| Evidence | Screenshots, HTML reports |

## Project Structure

```text
openmrs-healthcare-testing-project/
├── manual-testing/
├── selenium-ui-automation/
├── postman-api-testing/
└── evidence/
