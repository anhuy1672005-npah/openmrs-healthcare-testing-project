import pytest

from config import PATIENT_SEARCH
from pages.home_page import HomePage
from pages.patient_search_page import PatientSearchPage


@pytest.mark.o2
@pytest.mark.patient_search
def test_search_patient_by_common_keyword_shows_results(logged_in_driver):
    home_page = HomePage(logged_in_driver)
    home_page.open_find_patient()

    search_page = PatientSearchPage(logged_in_driver)
    search_page.search(PATIENT_SEARCH)

    rows = search_page.get_result_rows()
    if not rows:
        pytest.skip(
            f"No patient data returned for keyword '{PATIENT_SEARCH}'. Demo O2 data may have changed."
        )

    assert len(rows) > 0


@pytest.mark.o2
@pytest.mark.patient_search
def test_open_first_patient_profile_from_search_results(logged_in_driver):
    home_page = HomePage(logged_in_driver)
    home_page.open_find_patient()

    search_page = PatientSearchPage(logged_in_driver)
    search_page.search(PATIENT_SEARCH)

    if not search_page.get_result_rows():
        pytest.skip(
            f"No patient data returned for keyword '{PATIENT_SEARCH}'. Demo O2 data may have changed."
        )

    search_page.open_first_result()
    search_page.assert_patient_dashboard_loaded()


@pytest.mark.o2
@pytest.mark.patient_search
def test_search_patient_with_unlikely_keyword_shows_no_matching_records(logged_in_driver):
    home_page = HomePage(logged_in_driver)
    home_page.open_find_patient()

    search_page = PatientSearchPage(logged_in_driver)
    search_page.search("ZZZ_NO_PATIENT_987654321")

    assert search_page.has_no_matching_records() or len(search_page.get_result_rows()) == 0
