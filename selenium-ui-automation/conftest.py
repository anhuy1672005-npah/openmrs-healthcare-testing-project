from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import WebDriverException

from config import BROWSER, HEADLESS, LOCATION, PASSWORD, USERNAME
from pages.login_page import LoginPage


ROOT_DIR = Path(__file__).resolve().parent
EVIDENCE_DIR = ROOT_DIR.parent / "evidence" / "automation-report"
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)


def _chrome_driver() -> webdriver.Chrome:
    options = ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(options=options)


def _edge_driver() -> webdriver.Edge:
    options = EdgeOptions()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    return webdriver.Edge(options=options)


def _firefox_driver() -> webdriver.Firefox:
    options = FirefoxOptions()
    if HEADLESS:
        options.add_argument("--headless")
    return webdriver.Firefox(options=options)


@pytest.fixture
def driver():
    try:
        if BROWSER == "edge":
            drv = _edge_driver()
        elif BROWSER == "firefox":
            drv = _firefox_driver()
        else:
            drv = _chrome_driver()
    except WebDriverException as exc:
        pytest.fail(f"Cannot start browser '{BROWSER}'. Details: {exc}")

    drv.maximize_window()
    yield drv
    drv.quit()


@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(USERNAME, PASSWORD, LOCATION)
    login_page.assert_login_successful()
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    drv = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
    if drv is None:
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = item.name.replace("/", "_").replace("\\", "_")
    screenshot_path = EVIDENCE_DIR / f"{safe_name}_{timestamp}.png"
    try:
        drv.save_screenshot(str(screenshot_path))
    except Exception:
        pass
