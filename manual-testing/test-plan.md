# Test Plan

## 1. Project Overview

This project focuses on testing the OpenMRS Healthcare Web Application demo. OpenMRS is an electronic medical record system used to manage patient information and healthcare-related workflows.

The goal of this project is to simulate a practical QA process for a healthcare web application by combining manual testing, Selenium UI automation, and Postman API testing.

The testing scope focuses on key workflows such as login, logout, patient search, patient profile viewing, patient registration, form validation, and selected REST API checks related to authentication and patient/person data.

## 2. Testing Objectives

The main objectives of this test plan are:

1. Verify that users can log in and log out successfully.
2. Verify that the system handles invalid login attempts correctly.
3. Verify that users can search for patients by name or identifier.
4. Verify that users can open and view the correct patient profile.
5. Verify that users can register a new patient with valid required data.
6. Verify that the patient registration form handles missing or invalid required fields properly.
7. Verify selected OpenMRS REST API endpoints related to authentication, current user, patient/person search, patient/person detail, invalid request, and no-auth access observation.
8. Identify functional issues, usability issues, validation problems, or QA improvement points.
9. Select stable and important regression test cases for Selenium UI automation.

## 3. Scope

### 3.1 In Scope

The following modules and workflows are included in this project:

#### Manual Testing

- Login with valid credentials
- Login with invalid credentials
- Login with missing required input
- Location selection during login
- Logout
- Search patient by name or identifier
- Search patient with invalid or non-existing keyword
- Open patient profile from search results
- Verify patient profile information is displayed
- Register a new patient with valid required data
- Validate required fields in patient registration
- Validate invalid or incomplete patient registration data

#### Selenium UI Automation

The following stable regression flows are planned for automation:

- Successful login
- Failed login
- Logout
- Patient search
- Open patient profile from search results
- Required field validation in patient registration
- Optional: patient registration with valid test data

#### Postman API Testing

The following API areas are planned for basic API testing:

- Session/authentication check
- Current user check
- Patient/person search
- Patient/person detail by UUID
- Invalid UUID or not found case
- Unauthorized request
- Basic validation or error handling

### 3.2 Out of Scope

The following areas are not included in this project:

- Real patient data testing
- Database testing
- Performance or load testing
- Advanced security testing
- Mobile application testing
- Full clinical workflow testing
- Full system integration testing
- Automated CI/CD pipeline setup
- Testing all OpenMRS modules
- Testing production healthcare data

## 4. Test Environment

| Item | Description |
|---|---|
| Application Under Test | OpenMRS 2 Demo |
| Application Type | Healthcare / Electronic Medical Record Web Application |
| Test Data | Demo / anonymized patient data |
| User Role | Admin demo user |
| Username | admin |
| Password | Admin123 |
| Login Location | Any |
| Browser | Google Chrome |
| Operating System | Windows 10/11 |
| Manual Testing Tool | Google Sheets / Excel, Markdown |
| UI Automation Tools | Python, Selenium WebDriver, Pytest |
| API Testing Tool | Postman |
| Version Control | Git and GitHub |
| Evidence | Screenshots, test reports, API reports |

Note: The OpenMRS public demo environment may change over time. Test results may vary depending on demo data, server availability, and UI changes.

## 5. Test Approach

The project follows a step-by-step QA workflow:

1. Explore the OpenMRS demo application to understand the main workflows.
2. Identify modules, screens, user actions, expected results, and potential risks.
3. Create a test plan to define scope, objectives, tools, and risks.
4. Write test scenarios for each module in scope.
5. Write detailed manual test cases based on test scenarios.
6. Execute manual test cases and record actual results.
7. Capture screenshots as test evidence.
8. Document bugs, observed issues, or QA recommendations.
9. Select stable and important test cases for Selenium automation.
10. Implement Selenium UI automation using Python, Selenium WebDriver, Pytest, and Page Object Model.
11. Create Postman API test cases for selected OpenMRS REST API endpoints.
12. Run API tests and record results.
13. Create a traceability matrix to connect requirements, manual test cases, automation tests, and API tests.
14. Prepare the final test summary report.

## 6. Test Types

| Test Type | Purpose | Tool |
|---|---|---|
| Functional Testing | Verify that key OpenMRS workflows work as expected | Manual Testing |
| UI Testing | Verify user interface behavior and user interactions | Browser, Chrome DevTools |
| Negative Testing | Verify how the system handles invalid input or invalid actions | Manual Testing, Postman |
| Regression Testing | Re-run important test cases to ensure existing features still work | Selenium, Pytest |
| API Testing | Verify selected backend endpoints and response data | Postman |
| Validation Testing | Verify required fields and invalid data handling | Manual Testing, Selenium |
| Usability Observation | Identify UI/UX issues or improvement points | Manual Testing |

## 7. Test Data

The project uses only demo or dummy data.

### 7.1 Existing Demo Data

Existing anonymized patient data in the OpenMRS demo may be used for:

- Patient search
- Patient profile viewing
- Patient/person API search
- Patient/person detail retrieval

### 7.2 Dummy Test Data

Dummy test data may be used for patient registration.

Example:

| Field | Example Data |
|---|---|
| Given Name | TestAuto |
| Family Name | Patient |
| Gender | Male |
| Age | 30 |
| Address | Demo Address |
| Phone Number | 0123456789 |

Note: If testing on the public demo environment, avoid creating too much unnecessary data. For more stable testing, a local OpenMRS instance can be used.

## 8. Entry Criteria

Testing can start when:

1. The OpenMRS demo site is accessible.
2. Demo credentials are available and valid.
3. The browser and test environment are ready.
4. Project repository structure has been created.
5. Test scope has been defined.
6. Basic application exploration has been completed.
7. Screenshots or notes from application exploration are available.
8. Test plan has been reviewed and updated.

## 9. Exit Criteria

Testing can be considered complete when:

1. All planned manual test cases have been written.
2. All planned manual test cases have been executed.
3. Actual results and test statuses have been recorded.
4. Failed or blocked cases have been analyzed.
5. Bugs, observed issues, or QA recommendations have been documented.
6. Selected regression test cases have been automated with Selenium.
7. Selected API test cases have been created and executed in Postman.
8. Test evidence has been saved.
9. Traceability matrix has been updated.
10. Final test summary report has been completed.

## 10. Deliverables

The final project deliverables include:

1. Project overview
2. Test plan
3. Application map / exploration notes
4. Test scenarios
5. Manual test cases
6. Test execution results
7. Bug reports or QA recommendations
8. Traceability matrix
9. Selenium UI automation scripts
10. Pytest HTML report
11. Postman API collection
12. Postman environment
13. API test summary
14. Manual screenshots and evidence
15. Final test summary report
16. GitHub README

## 11. Roles and Responsibilities

Since this is an individual portfolio project, the tester is responsible for:

| Role | Responsibility |
|---|---|
| QA Tester | Explore application, write test plan, test scenarios, test cases, execute tests |
| Automation Tester | Implement Selenium UI automation for selected regression cases |
| API Tester | Create and execute Postman API test cases |
| Documentation Owner | Maintain README, reports, evidence, and traceability matrix |

## 12. Risks and Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| Public demo environment may be unstable | Test execution may be blocked or inconsistent | Record the issue and retry later |
| Demo data may change or reset | Search results or patient data may differ | Use flexible test data and document assumptions |
| UI elements may change | Selenium locators may fail | Prefer stable locators and update Page Object files |
| API endpoints may require authentication | API tests may fail without valid credentials/session | Use proper Basic Auth or session setup in Postman |
| Patient registration may create unwanted demo data | Public demo may become messy | Use minimal dummy data and avoid excessive create tests |
| Not all bugs are reproducible | Bug reports may be weak | Document observed issues or QA recommendations instead of inventing bugs |
| Scope may become too large | Project may become unfinished | Focus only on login, patient search, profile, registration, validation, and selected API checks |

## 13. Assumptions

The project is based on the following assumptions:

1. The OpenMRS demo environment is available during testing.
2. The demo account is allowed for learning and exploration.
3. Demo/anonymized patient data can be used for testing.
4. The project does not involve real patient data.
5. The project focuses on functional testing, UI automation, and basic API testing.
6. Public demo behavior may change over time, so test evidence and results are captured during execution.

## 14. Test Schedule

| Phase | Activity | Output |
|---|---|---|
| Phase 1 | Project setup | GitHub repo and folder structure |
| Phase 2 | Application exploration | Application map, screenshots, test ideas |
| Phase 3 | Test planning | Test plan |
| Phase 4 | Test scenario design | Test scenarios |
| Phase 5 | Manual test case design | Manual test cases |
| Phase 6 | Manual test execution | Test results and evidence |
| Phase 7 | Bug / issue documentation | Bug reports or QA recommendations |
| Phase 8 | Selenium automation | Automation scripts and Pytest report |
| Phase 9 | Postman API testing | API collection and API summary |
| Phase 10 | Final documentation | Test summary report and README update |

## 15. Approval

This test plan is created for a personal QA portfolio project. It will be updated when the test scope, environment, or implementation changes.
