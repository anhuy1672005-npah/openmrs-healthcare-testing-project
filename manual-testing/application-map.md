# OpenMRS Application Map

## 1. Test Environment

| Item | Description |
|---|---|
| Application | OpenMRS 2 Demo |
| URL | OpenMRS official demo |
| User role | Admin demo user |
| Username | admin |
| Password | Admin123 |
| Location | Any |
| Browser | Google Chrome |
| OS | Windows 10/11 |
| Testing date | 2026-07-06 |

## 2. Main Modules in Scope

| Module | Screen / Feature | In Scope? | Reason |
|---|---|---|---|
| Login | Login page and location selection | Yes | Required to access the system |
| Home Dashboard | Main dashboard after login | Yes | Entry point after successful login |
| Find Patient Record | Patient search screen | Yes | Critical workflow for healthcare users |
| Patient Profile | Patient details page | Yes | Used to view patient information |
| Register a Patient | Patient registration form | Yes | Important data entry workflow |
| Logout | End user session | Yes | Basic authentication workflow |

## 3. Login Flow Observation

### 3.1 Valid Login Flow

| Step | User Action | System Behavior |
|---|---|---|
| 1 | Open OpenMRS 2 demo login page | Login page is displayed |
| 2 | Enter valid username | Username is accepted |
| 3 | Enter valid password | Password is accepted |
| 4 | Select location | Location is selected |
| 5 | Click Login | User is redirected to the home dashboard |

### 3.2 Possible Test Ideas

| Test Idea ID | Test Idea |
|---|---|
| TI_LOGIN_001 | Login with valid username, password, and location |
| TI_LOGIN_002 | Login with invalid password |
| TI_LOGIN_003 | Login with empty username |
| TI_LOGIN_004 | Login with empty password |
| TI_LOGIN_005 | Login without selecting location |
| TI_LOGIN_006 | Verify logout after successful login |

## 4. Patient Search Flow Observation

### 4.1 Normal Search Flow

| Step | User Action | System Behavior |
|---|---|---|
| 1 | Open Find Patient Record | Patient search page is displayed |
| 2 | Enter patient name or ID | System displays matching patient records |
| 3 | Select a patient from search results | Patient profile page is opened |

### 4.2 Possible Test Ideas

| Test Idea ID | Test Idea |
|---|---|
| TI_SEARCH_001 | Search patient by valid name |
| TI_SEARCH_002 | Search patient by valid patient identifier |
| TI_SEARCH_003 | Search with non-existing keyword |
| TI_SEARCH_004 | Search with empty input |
| TI_SEARCH_005 | Search with special characters |
| TI_SEARCH_006 | Open patient profile from search result |

## 5. Patient Profile Observation

### 5.1 Displayed Information

| Information | Displayed? | Notes |
|---|---|---|
| Patient name | Yes | To be confirmed |
| Patient identifier | Yes | To be confirmed |
| Gender | Yes | To be confirmed |
| Age / Birthdate | Yes | To be confirmed |
| Visits / Encounters | Yes/No | To be confirmed |
| Allergies / Conditions | Yes/No | To be confirmed |

### 5.2 Possible Test Ideas

| Test Idea ID | Test Idea |
|---|---|
| TI_PROFILE_001 | Verify patient profile opens after selecting a search result |
| TI_PROFILE_002 | Verify patient name is displayed on profile page |
| TI_PROFILE_003 | Verify patient identifier is displayed |
| TI_PROFILE_004 | Verify navigation back to search or dashboard |

## 6. Patient Registration Flow Observation

### 6.1 Main Steps

| Step | Section | Observation |
|---|---|---|
| 1 | Name | User enters given name and family name |
| 2 | Gender | User selects gender |
| 3 | Birthdate / Age | User enters birthdate or age |
| 4 | Address | User enters address information |
| 5 | Phone Number | User enters phone number if available |
| 6 | Relatives | User may enter relationship information |
| 7 | Confirmation | System displays entered information for confirmation |
| 8 | Submit | New patient record is created |

### 6.2 Possible Test Ideas

| Test Idea ID | Test Idea |
|---|---|
| TI_REGISTER_001 | Register patient with valid required data |
| TI_REGISTER_002 | Register patient without given name |
| TI_REGISTER_003 | Register patient without family name |
| TI_REGISTER_004 | Register patient without gender |
| TI_REGISTER_005 | Register patient with invalid birthdate |
| TI_REGISTER_006 | Verify confirmation page before submit |
| TI_REGISTER_007 | Verify patient profile after successful registration |

## 7. Logout Flow Observation

| Step | User Action | System Behavior |
|---|---|---|
| 1 | User clicks Logout | User is logged out |
| 2 | System redirects to login page | Login page is displayed |
| 3 | User tries browser Back button | Protected page should not be accessible without login |

## Possible Test Ideas

| Test Idea ID | Test Idea |
|---|---|
| TI_LOGOUT_001 | Verify logout after successful login |
| TI_LOGOUT_002 | Verify user cannot access protected page after logout |

## 8. UI Elements for Future Automation

| Page | Element | Possible Locator | Notes |
|---|---|---|---|
| Login | Username input | To be inspected | Prefer ID/name if available |
| Login | Password input | To be inspected | Prefer ID/name if available |
| Login | Location selector | To be inspected | May need click by visible text |
| Login | Login button | To be inspected | Avoid unstable XPath |
| Patient Search | Search input | To be inspected | Used for patient search automation |
| Register Patient | Given name field | To be inspected | Required field |

## 9. API / Network Observation

| UI Flow | Possible API / Request | Method | Status | Notes |
|---|---|---|---|---|
| Login | Session/authentication request | GET/POST | To be confirmed | Used for API auth testing |
| Search patient | Patient/person search request | GET | To be confirmed | Can be tested in Postman |
| Open patient profile | Patient/person detail request | GET | To be confirmed | May use UUID |
| Logout | Session end request | DELETE/POST | To be confirmed | Used for session testing |

## 10. Initial Test Ideas

| Test Idea ID | Module | Test Idea | Priority | Candidate for Automation | Candidate for API Test |
|---|---|---|---|---|---|
| TI_LOGIN_001 | Login | Login with valid credentials and location | High | Yes | Yes |
| TI_LOGIN_002 | Login | Login with invalid password | High | Yes | Yes |
| TI_LOGIN_003 | Login | Login with empty username | Medium | Yes | No |
| TI_LOGIN_004 | Login | Login without selecting location | Medium | Yes | No |
| TI_SEARCH_001 | Patient Search | Search patient by valid name | High | Yes | Yes |
| TI_SEARCH_002 | Patient Search | Search patient by patient identifier | High | Yes | Yes |
| TI_SEARCH_003 | Patient Search | Search with non-existing keyword | Medium | Yes | Yes |
| TI_PROFILE_001 | Patient Profile | Open patient profile from search result | High | Yes | Yes |
| TI_PROFILE_002 | Patient Profile | Verify patient name and identifier are displayed | High | Yes | Yes |
| TI_REGISTER_001 | Register Patient | Register patient with valid required data | High | Optional | Optional |
| TI_REGISTER_002 | Register Patient | Validate required name fields | High | Yes | Optional |
| TI_REGISTER_003 | Register Patient | Validate required gender field | High | Yes | Optional |
| TI_REGISTER_004 | Register Patient | Validate invalid birthdate or age | Medium | Optional | Optional |
| TI_LOGOUT_001 | Logout | Logout from the system | High | Yes | Yes |
| TI_LOGOUT_002 | Logout | Verify protected page after logout | Medium | Optional | Yes |
