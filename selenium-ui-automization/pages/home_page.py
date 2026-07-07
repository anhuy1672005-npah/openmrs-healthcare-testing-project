from __future__ import annotations

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from config import FIND_PATIENT_PATH, HOME_PATH, REGISTER_PATIENT_PATH
from pages.base_page import BasePage


class HomePage(BasePage):
    FIND_PATIENT_TILE = (
        By.XPATH,
        "//a[contains(normalize-space(.), 'Find Patient Record') or contains(@href, 'findPatient')]",
    )
    REGISTER_PATIENT_TILE = (
        By.XPATH,
        "//a[contains(normalize-space(.), 'Register a patient') or contains(@href, 'registerPatient')]",
    )
    LOGOUT_LINK = (By.XPATH, "//a[contains(@href, 'logout') or normalize-space(.)='Logout']")

    def open(self) -> None:
        self.open_url(HOME_PATH)

    def open_find_patient(self) -> None:
        try:
            self.click(self.FIND_PATIENT_TILE, timeout=5)
        except TimeoutException:
            # Direct O2 URL keeps tests stable if the tile id/text changes.
            self.open_url(FIND_PATIENT_PATH)

    def open_register_patient(self) -> None:
        try:
            self.click(self.REGISTER_PATIENT_TILE, timeout=5)
        except TimeoutException:
            self.open_url(REGISTER_PATIENT_PATH)

    def logout(self) -> None:
        self.click(self.LOGOUT_LINK, timeout=8)
