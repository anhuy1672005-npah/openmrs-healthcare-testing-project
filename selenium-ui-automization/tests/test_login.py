import pytest

from config import LOCATION, PASSWORD, USERNAME
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.o2
@pytest.mark.login
def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(USERNAME, PASSWORD, LOCATION)

    login_page.assert_login_successful()


@pytest.mark.o2
@pytest.mark.login
def test_login_with_invalid_password_shows_error(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(USERNAME, "WrongPassword123", LOCATION)

    assert login_page.is_on_login_page(), "Invalid password should not allow user to leave login page."
    error_text = login_page.get_error_text().lower()
    assert any(keyword in error_text for keyword in ["invalid", "error", "try again", "login", "password"])


@pytest.mark.o2
@pytest.mark.login
def test_logout_returns_user_to_login_page(logged_in_driver):
    home_page = HomePage(logged_in_driver)
    home_page.logout()

    login_page = LoginPage(logged_in_driver)
    assert login_page.is_on_login_page()
