"""Configuration for OpenMRS O2 Selenium tests.

This framework targets OpenMRS O2 / Reference Application 2.x, not O3.
Default URL: https://o2.openmrs.org/openmrs

Environment variables can override all values. Copy `.env.example` to `.env`
for local execution if needed.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - dependency is declared in requirements.txt
    load_dotenv = None

if load_dotenv:
    load_dotenv(Path(__file__).resolve().parent / ".env")


def _bool_env(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


BASE_URL = os.getenv("OPENMRS_BASE_URL", "https://o2.openmrs.org/openmrs").rstrip("/")
USERNAME = os.getenv("OPENMRS_USERNAME", "admin")
PASSWORD = os.getenv("OPENMRS_PASSWORD", "Admin123")
LOCATION = os.getenv("OPENMRS_LOCATION", "Registration Desk")
BROWSER = os.getenv("BROWSER", "chrome").strip().lower()
HEADLESS = _bool_env("HEADLESS", False)
TIMEOUT = int(os.getenv("SELENIUM_TIMEOUT", "20"))
PATIENT_SEARCH = os.getenv("OPENMRS_PATIENT_SEARCH", "a")
RUN_REGISTRATION_TESTS = _bool_env("RUN_REGISTRATION_TESTS", False)

# Relative O2 URLs. Keeping these in config makes it clear this is not O3 SPA.
LOGIN_PATH = "/login.htm"
HOME_PATH = "/referenceapplication/home.page"
FIND_PATIENT_PATH = "/coreapps/findpatient/findPatient.page?app=coreapps.findPatient"
REGISTER_PATIENT_PATH = "/registrationapp/registerPatient.page?appId=referenceapplication.registrationapp.registerPatient"
