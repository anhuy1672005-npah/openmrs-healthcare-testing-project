# Selenium Automation Report Evidence

This folder stores Pytest HTML reports and failure screenshots generated during Selenium execution.

Recommended command from `selenium-ui-automation/`:

```powershell
pytest -m "not registration" --html=../evidence/automation-report/selenium-report.html --self-contained-html
```

Regenerate `selenium-report.html` after code or configuration changes so the report matches the current test suite.
