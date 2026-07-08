# OpenMRS Healthcare Web Testing Project

## 1. Project Name

OpenMRS Healthcare Web Testing Project: Manual Testing, Selenium UI Automation, and Postman API Testing

## 2. Background

OpenMRS is an open-source electronic medical record system used to manage patient information and clinical workflows. In healthcare software, system reliability, data accuracy, and usability are important because users rely on the system to search, view, and manage patient records.

This project uses the OpenMRS O2 demo application to simulate a practical QA workflow for a healthcare web application.

## 3. Problem Statement

Healthcare web applications need to be reliable and easy to use. Errors in authentication, patient search, patient registration, or data validation may affect user experience and data quality.

This project focuses on testing critical OpenMRS workflows, documenting public-demo limitations, and showing how manual testing, UI automation, and API testing can support software quality.

## 4. Testing Objectives

The objectives of this project are:

1. Verify that users can log in and log out successfully.
2. Verify that users can search for patients and open a patient profile when stable demo data is available.
3. Verify patient registration page access and safe name-step checks without creating unnecessary records in the shared public demo.
4. Verify that negative and incomplete input scenarios are designed and documented for manual or future local-environment execution.
5. Validate selected OpenMRS REST API endpoints related to authentication, user/location lookup, patient search, patient detail retrieval, and error/observation handling.
6. Automate selected stable regression test cases using Selenium WebDriver, Python, and Pytest.

## 5. In Scope

This project covers the following modules and workflows:

### Manual Testing

- Login with valid and invalid credentials
- Location selection after login
- Logout
- Search patient by name or identifier
- Open patient profile from search results
- Patient registration test design for valid and negative data-entry scenarios
- Required-field and invalid-input validation scenarios

### Selenium UI Automation

- O2 login page availability
- Successful login
- Failed login
- Logout
- Patient search with a common demo keyword
- Open first patient profile when search results exist
- Patient search with an unlikely keyword and no-result validation
- Optional patient registration page access and name-step progression check

### Postman API Testing

- Authentication/session behavior
- Invalid credential behavior
- User search
- Login location search
- Patient search
- Patient detail retrieval when a UUID is available
- Invalid UUID robustness observation
- No-auth patient search access-control observation

## 6. Out of Scope

The following areas are not included in this project:

- Real patient data testing
- Database testing
- Performance/load testing
- Advanced security testing
- Mobile application testing
- Full clinical workflow testing
- Full patient-registration submission on the shared public demo
- Full system integration testing
- CI/CD pipeline setup in the initial version

## 7. Test Environment

Initial testing is performed on the OpenMRS O2 public demo environment.

- Application: OpenMRS O2 Demo / Reference Application 2.x
- Browser: Google Chrome
- Operating System: Windows 10/11
- Manual Testing Tool: Google Sheets / Excel
- UI Automation: Python, Selenium WebDriver, Pytest
- API Testing: Postman
- Version Control: Git and GitHub

Note: Since the public demo environment may change over time, test data and results may vary. For stable full registration and repeatable patient-profile testing, a local OpenMRS instance should be used.

## 8. Tools Used

| Tool | Purpose |
|---|---|
| OpenMRS O2 Demo | System under test |
| Google Sheets / Excel | Manual test case design and execution tracking |
| Markdown | Test documentation |
| GitHub | Version control and portfolio hosting |
| Chrome DevTools | Inspecting elements and debugging UI/API behavior |
| Python | Programming language for UI automation |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution and reporting |
| Postman | API testing |
| Newman / Postman CLI | Optional API test execution from command line |

## 9. Deliverables

The project includes:

1. Project overview
2. Test plan
3. Test scenarios
4. Manual test cases
5. Manual execution status workbook
6. QA observations and recommendations
7. Traceability matrix
8. Selenium UI automation scripts
9. Pytest HTML report output path
10. Postman API collection and environment
11. API test summary
12. Final test summary report
13. Evidence reports and optional manual screenshots

## 10. Risks and Limitations

- The public demo environment may be unstable or change over time.
- Demo patient data may be updated or reset.
- Patient search/profile automation can skip when the configured search keyword returns no results.
- Some UI elements may change, causing Selenium locators to fail.
- API endpoints may return public-demo-specific behavior such as `500` for invalid UUID or `200` for no-auth patient search.
- This project uses demo/anonymized data only and does not involve real patient data.
- The project focuses on functional testing, UI automation, and basic API testing, not advanced clinical validation.

## 11. Expected Outcome

The repository demonstrates basic QA planning, test design, UI automation, API testing, and reporting for a healthcare web application. The project keeps the scope intentionally small and clearly documents skipped tests, blocked data-dependent cases, and public-demo limitations.
