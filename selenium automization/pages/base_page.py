from __future__ import annotations

from typing import Iterable, Sequence

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL, TIMEOUT

Locator = tuple[str, str]


def xpath_literal(text: str) -> str:
    """Return a safe XPath string literal for text with quotes."""
    if "'" not in text:
        return f"'{text}'"
    if '"' not in text:
        return f'"{text}"'
    parts = text.split("'")
    return "concat(" + ", \"'\", ".join(f"'{part}'" for part in parts) + ")"


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = TIMEOUT):
        self.driver = driver
        self.timeout = timeout

    def open_url(self, path_or_url: str) -> None:
        if path_or_url.startswith("http"):
            self.driver.get(path_or_url)
        else:
            self.driver.get(f"{BASE_URL}{path_or_url}")

    def wait_visible(self, locator: Locator, timeout: int | None = None) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_present(self, locator: Locator, timeout: int | None = None) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_clickable(self, locator: Locator, timeout: int | None = None) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def find_visible_first(self, locators: Sequence[Locator], timeout_per_locator: int = 4) -> WebElement:
        last_error: Exception | None = None
        for locator in locators:
            try:
                return self.wait_visible(locator, timeout_per_locator)
            except Exception as exc:
                last_error = exc
        raise TimeoutException(f"No visible element found for locators: {locators}") from last_error

    def click(self, locator: Locator, timeout: int | None = None) -> None:
        element = self.wait_clickable(locator, timeout)
        self.safe_click_element(element)

    def click_first(self, locators: Sequence[Locator], timeout_per_locator: int = 4) -> None:
        last_error: Exception | None = None
        for locator in locators:
            try:
                element = self.wait_clickable(locator, timeout_per_locator)
                self.safe_click_element(element)
                return
            except Exception as exc:
                last_error = exc
        raise TimeoutException(f"None of these locators were clickable: {locators}") from last_error

    def safe_click_element(self, element: WebElement) -> None:
        try:
            element.click()
        except WebDriverException:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator: Locator, text: str, clear: bool = True) -> None:
        element = self.wait_visible(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def elements(self, locator: Locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def is_visible(self, locator: Locator, timeout: int = 3) -> bool:
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def page_contains_text(self, text: str, timeout: int = 5) -> bool:
        literal = xpath_literal(text)
        try:
            self.wait_visible((By.XPATH, f"//*[contains(normalize-space(.), {literal})]"), timeout)
            return True
        except TimeoutException:
            return False
