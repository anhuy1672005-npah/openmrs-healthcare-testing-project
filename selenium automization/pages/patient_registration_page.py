from __future__ import annotations

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from config import REGISTER_PATIENT_PATH
from pages.base_page import BasePage


class PatientRegistrationPage(BasePage):
    """Page object for the OpenMRS O2 patient registration wizard.

    Registration on the public O2 demo is intentionally treated as optional in
    this project because it can create data in a shared demo environment and the
    wizard may differ slightly between demo resets. These locators therefore use
    several stable fallbacks instead of relying on one generated id.
    """

    GIVEN_NAME = (
        By.CSS_SELECTOR,
        "input[name='givenName'], input[name*='givenName'], input[id$='givenName-field'], input[id*='givenName']",
    )
    FAMILY_NAME = (
        By.CSS_SELECTOR,
        "input[name='familyName'], input[name*='familyName'], input[id$='familyName-field'], input[id*='familyName']",
    )

    NEXT_BUTTON_LOCATORS = [
        (By.ID, "next-button"),
        (By.CSS_SELECTOR, "#next-button, button#next-button, input#next-button, a#next-button"),
        (By.CSS_SELECTOR, "button.confirm, input.confirm, a.confirm"),
        (By.XPATH, "//button[normalize-space(.)='Next']"),
        (By.XPATH, "//a[normalize-space(.)='Next']"),
        (By.XPATH, "//input[@value='Next']"),
        (
            By.XPATH,
            "//*[self::button or self::a or self::input][contains(translate(normalize-space(.), 'NEXT', 'next'), 'next') or translate(@value, 'NEXT', 'next')='next']",
        ),
    ]

    CONFIRM_BUTTON = (
        By.CSS_SELECTOR,
        "input#submit, button#submit, input.submitButton, button.submitButton, button.confirm, input.confirm",
    )
    CANCEL_BUTTON = (By.XPATH, "//*[normalize-space(.)='Cancel' or contains(@class, 'cancel')]")
    VALIDATION_ERROR = (
        By.XPATH,
        "//*[contains(@class, 'field-error') or contains(@class, 'error') or contains(normalize-space(.), 'Required') or contains(normalize-space(.), 'required')]",
    )
    PAGE_TITLE = (
        By.XPATH,
        "//*[contains(normalize-space(.), 'Register a patient') or contains(normalize-space(.), 'Name')]",
    )

    def open(self) -> None:
        self.open_url(REGISTER_PATIENT_PATH)
        self.wait_visible(self.PAGE_TITLE, timeout=12)

    def _type_and_fire_events(self, locator: tuple[str, str], text: str) -> WebElement:
        """Type text and fire JS events so the wizard validator notices it."""
        element = self.wait_visible(locator, timeout=10)
        element.clear()
        element.send_keys(text)
        self.driver.execute_script(
            """
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            arguments[0].blur();
            """,
            element,
        )
        return element

    def fill_required_name(self, given_name: str, family_name: str) -> None:
        self._type_and_fire_events(self.GIVEN_NAME, given_name)
        self._type_and_fire_events(self.FAMILY_NAME, family_name)

    def visible_next_buttons(self) -> list[WebElement]:
        candidates: list[WebElement] = []
        for locator in self.NEXT_BUTTON_LOCATORS:
            try:
                for element in self.elements(locator):
                    if element.is_displayed() and element not in candidates:
                        candidates.append(element)
            except WebDriverException:
                continue
        return candidates

    def click_next_if_available(self) -> bool:
        """Click Next when the O2 wizard exposes an enabled Next button.

        Returns False instead of raising when the public demo does not expose an
        enabled Next button. This keeps the optional registration tests honest:
        page access can still be verified, while unstable data-creation steps do
        not create false failures in the portfolio report.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        for element in self.visible_next_buttons():
            try:
                if not element.is_enabled():
                    continue
                self.safe_click_element(element)
                return True
            except WebDriverException:
                continue
        return False

    def click_next(self) -> None:
        if not self.click_next_if_available():
            raise TimeoutException("No enabled Next button was available on the O2 registration wizard.")

    def has_validation_error(self) -> bool:
        return self.is_visible(self.VALIDATION_ERROR, timeout=8)

    def assert_registration_page_open(self) -> None:
        self.wait_visible(self.PAGE_TITLE, timeout=12)
