# OpenMRS Healthcare Web Testing Project

## 1. Project Name

OpenMRS Healthcare Web Testing Project: Manual Testing, Selenium UI Automation, and Postman API Testing

## 2. Background

OpenMRS is an open-source electronic medical record system used to manage patient information and clinical workflows. In healthcare software, system reliability, data accuracy, and usability are important because users rely on the system to search, view, and manage patient records.

This project uses the OpenMRS demo application to simulate a real QA process for a healthcare web application.

## 3. Problem Statement

Healthcare web applications need to be reliable and easy to use. Errors in authentication, patient search, patient registration, or data validation may affect user experience and data quality.

This project focuses on testing critical OpenMRS workflows to identify functional issues, validate expected behavior, and demonstrate how manual testing, UI automation, and API testing can support software quality.

## 4. Testing Objectives

The objectives of this project are:

1. Verify that users can log in and log out successfully.
2. Verify that users can search for patients and open the correct patient profile.
3. Verify that users can register a new patient with valid data.
4. Verify that required fields and invalid inputs are handled properly.
5. Validate selected OpenMRS REST API endpoints related to authentication, patient/person search, data retrieval, and error handling.
6. Automate selected stable regression test cases using Selenium WebDriver, Python, and Pytest.

## 5. In Scope

This project covers the following modules and workflows:

### Manual Testing

- Login with valid and invalid credentials
- Location selection after login
- Logout
- Search patient by name or identifier
- Open patient profile from search results
- Register a new patient with valid data
- Validate required fields in the patient registration form
- Validate invalid or incomplete input data

### Selenium UI Automation

- Successful login
- Failed login
- Logout
- Patient search
- Open patient profile
- Patient registration with valid data
- Required field validation

### Postman API Testing

- Authentication/session check
- Get current user
- Search person/patient
- Get patient/person details by UUID
- Invalid UUID or not found case
- Unauthorized request
- Basic validation/error handling

## 6. Out of Scope

The following areas are not included in this project:

- Real patient data testing
- Database testing
- Performance/load testing
- Advanced security testing
- Mobile application testing
- Full clinical workflow testing
- Full system integration testing
- CI/CD pipeline setup in the initial version

## 7. Test Environment

Initial testing will be performed on the OpenMRS demo environment.

- Application: OpenMRS Demo
- Browser: Google Chrome
- Operating System: Windows 10/11
- Manual Testing Tool: Google Sheets / Excel
- UI Automation: Python, Selenium WebDriver, Pytest
- API Testing: Postman
- Version Control: Git and GitHub

Note: Since the public demo environment may change over time, test data and results may vary. For a more stable automation setup, a local OpenMRS standalone instance can be used.

## 8. Tools Used

| Tool | Purpose |
|---|---|
| OpenMRS Demo | System under test |
| Google Sheets / Excel | Manual test case design and execution tracking |
| Markdown | Test documentation |
| GitHub | Version control and portfolio hosting |
| GitHub Issues | Bug and improvement tracking |
| Chrome DevTools | Inspecting elements and debugging UI/API behavior |
| Python | Programming language for UI automation |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution and reporting |
| Postman | API testing |
| Newman / Postman CLI | Optional API test execution from command line |

## 9. Deliverables

The final project will include:

1. Project overview
2. Test plan
3. Test scenarios
4. Manual test cases
5. Test execution results
6. Bug reports or QA recommendations
7. Traceability matrix
8. Selenium UI automation scripts
9. Pytest HTML report
10. Postman API collection and environment
11. API test summary
12. Final test summary report
13. Evidence screenshots

## 10. Risks and Limitations

- The public demo environment may be unstable or change over time.
- Demo patient data may be updated or reset.
- Some UI elements may change, causing Selenium locators to fail.
- API endpoints may require authentication or specific UUIDs.
- This project uses demo/anonymized data only and does not involve real patient data.
- The project focuses on functional testing, UI automation, and basic API testing, not advanced clinical validation.

## 11. Expected Outcome

After completing this project, the repository will demonstrate the ability to plan, design, execute, automate, and report testing activities for a healthcare web application. It will show practical QA skills across manual testing, UI automation testing, and API testing.
