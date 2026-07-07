import pytest

from pages.login_page import LoginPage


@pytest.mark.o2
@pytest.mark.smoke
def test_o2_login_page_loads(driver):
    login_page = LoginPage(driver)
    login_page.open()

    assert login_page.is_on_login_page()
    assert login_page.page_contains_text("Location for this session")
    assert login_page.page_contains_text("Registration Desk")
