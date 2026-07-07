from __future__ import annotations

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import FIND_PATIENT_PATH
from pages.base_page import BasePage


class PatientSearchPage(BasePage):
    SEARCH_INPUT = (By.ID, "patient-search")
    RESULTS_TABLE = (By.ID, "patient-search-results-table")
    RESULT_ROWS = (By.CSS_SELECTOR, "#patient-search-results-table tbody tr")
    EMPTY_RESULT_TEXT = (
        By.XPATH,
        "//*[contains(normalize-space(.), 'No matching records') or contains(normalize-space(.), 'No data available')]",
    )
    PATIENT_DASHBOARD_INDICATOR = (
        By.XPATH,
        "//*[contains(@class, 'patient-header') or contains(@class, 'demographics') or contains(normalize-space(.), 'Patient ID')]",
    )

    def open(self) -> None:
        self.open_url(FIND_PATIENT_PATH)
        self.wait_visible(self.SEARCH_INPUT)

    def search(self, keyword: str) -> None:
        field = self.wait_visible(self.SEARCH_INPUT)
        field.clear()
        field.send_keys(keyword)
        # O2 DataTables searches as user types. ENTER also works in many builds.
        field.send_keys(Keys.ENTER)
        self.wait_visible(self.RESULTS_TABLE)

    def get_result_rows(self) -> list:
        rows = self.elements(self.RESULT_ROWS)
        return [row for row in rows if row.is_displayed() and row.text.strip()]

    def has_no_matching_records(self) -> bool:
        return self.is_visible(self.EMPTY_RESULT_TEXT, timeout=5)

    def open_first_result(self) -> None:
        rows = self.get_result_rows()
        if not rows:
            raise TimeoutException("No patient rows available to open.")
        self.safe_click_element(rows[0])

    def assert_patient_dashboard_loaded(self) -> None:
        self.wait_visible(self.PATIENT_DASHBOARD_INDICATOR, timeout=12)
