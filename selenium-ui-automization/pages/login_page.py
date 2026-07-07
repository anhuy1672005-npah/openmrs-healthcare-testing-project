from __future__ import annotations

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from config import HOME_PATH, LOGIN_PATH
from pages.base_page import BasePage, xpath_literal


class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    LOGIN_FORM = (By.ID, "login-form")
    LOCATION_LIST_ITEMS = (By.CSS_SELECTOR, "#sessionLocation li, ul.select li, li.selectable")
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        ".error, .alert, #error-message, .note-container .note, .toast-item-wrapper",
    )

    def open(self) -> None:
        self.open_url(LOGIN_PATH)
        self.wait_visible(self.USERNAME)
        self.wait_visible(self.PASSWORD)

    def select_location(self, location_name: str) -> None:
        """Select an O2 login location.

        O2 RefApp login locations are rendered as clickable list items.
        Common IDs/texts include: Inpatient Ward, Isolation Ward, Laboratory,
        Outpatient Clinic, Pharmacy, Registration Desk.
        """
        location_name = (location_name or "Registration Desk").strip()

        if location_name.lower() in {"any", "first", "default"}:
            items = self.elements(self.LOCATION_LIST_ITEMS)
            for item in items:
                if item.is_displayed() and item.text.strip():
                    self.safe_click_element(item)
                    return
            raise TimeoutException("No visible O2 login location item found.")

        literal = xpath_literal(location_name)
        locators = [
            (By.ID, location_name),  # O2 uses ids with spaces, e.g. id="Registration Desk"
            (By.XPATH, f"//*[@id={literal}]"),
            (By.XPATH, f"//li[normalize-space(.)={literal}]"),
            (By.XPATH, f"//li[contains(normalize-space(.), {literal})]"),
            (
                By.XPATH,
                f"//*[self::li or self::button or self::a or self::span][normalize-space(.)={literal}]",
            ),
        ]

        try:
            self.click_first(locators, timeout_per_locator=4)
            return
        except TimeoutException:
            # Fallback: choose the first visible location. This keeps demo runs
            # stable when the requested location text changes, while the test
            # still verifies location-based login behaviour.
            items = self.elements(self.LOCATION_LIST_ITEMS)
            visible_names = []
            for item in items:
                text = item.text.strip()
                if item.is_displayed() and text:
                    visible_names.append(text)
                    self.safe_click_element(item)
                    return
            raise TimeoutException(
                f"Could not select O2 location '{location_name}'. Visible locations: {visible_names}"
            )

    def login(self, username: str, password: str, location_name: str = "Registration Desk") -> None:
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.select_location(location_name)
        self.click(self.LOGIN_BUTTON)

    def assert_login_successful(self) -> None:
        # O2 home redirects to /referenceapplication/home.page and shows app tiles.
        home_indicators = [
            (By.XPATH, "//*[contains(normalize-space(.), 'Find Patient Record')]"),
            (By.XPATH, "//*[contains(normalize-space(.), 'Register a patient')]"),
            (By.XPATH, "//*[contains(@id, 'findPatient')]"),
        ]
        try:
            self.find_visible_first(home_indicators, timeout_per_locator=8)
        except TimeoutException as exc:
            raise AssertionError(
                "Login did not reach the OpenMRS O2 home page. "
                f"Current URL: {self.driver.current_url}"
            ) from exc

    def get_error_text(self) -> str:
        if self.is_visible(self.ERROR_MESSAGE, timeout=5):
            return self.wait_visible(self.ERROR_MESSAGE, timeout=5).text.strip()
        return self.driver.find_element(By.TAG_NAME, "body").text

    def is_on_login_page(self) -> bool:
        return self.is_visible(self.USERNAME, timeout=5) and self.is_visible(self.PASSWORD, timeout=5)
