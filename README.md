```markdown
# Test Automation Framework

## Overview
This is a **Test Automation Framework** built using **Python** and **Playwright**. It follows the **Page Object Model (POM)** design pattern to ensure maintainability, scalability, and readability of the test scripts. The framework is designed to automate web applications and supports multiple browsers, including **Chromium**, **Firefox**, **WebKit**, and **Microsoft Edge**.

## Stack of Technologies
- **Programming Language**: Python
- **Automation Tool**: Playwright
- **Design Pattern**: Page Object Model (POM)
- **Test Runner**: Pytest
- **Reporting**: Allure Reports
- **Logging**: Python's built-in logging module

## Features
- Cross-browser testing support
- Headless and graphical (headed) browser modes
- Customizable browser options via command-line arguments
- Allure report integration for detailed test reporting
- Automatic screenshot capture on test failure

## Project Structure
- `pages/`: Contains Page Object Model classes for different pages.
- `tests/`: Contains test scripts organized by functionality.
- `conftest.py`: Contains shared fixtures and browser setup logic.
- `pytest.ini`: Configuration for Pytest markers.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## How to Run Tests

### Prerequisites
1. Install Python (>= 3.8).
2. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```bash
   playwright install
   ```

### Running Tests in Graphical Mode
To run tests in graphical (headed) mode and generate Allure reports:
```bash
pytest -m <marker> --custom-browser <browser> --alluredir=allure-results
```
Example:
```bash
pytest -m regressiontest --custom-browser firefox --alluredir=allure-results
```

### Running Tests in Headless Mode
To run tests in headless mode and generate Allure reports:
```bash
pytest -m <marker> --custom-browser <browser> --headless --alluredir=allure-results
```
Example:
```bash
pytest -m regressiontest --custom-browser firefox --headless --alluredir=allure-results
```

### Supported Browsers
- `chromium`
- `firefox`
- `webkit`
- `msedge`

### Markers
- `smoketest`: For smoke tests.
- `regressiontest`: For regression tests.
- `bookspageregressiontest`: For Books page-specific regression tests.

## Reporting
To generate and view Allure reports:
1. Run tests with Allure enabled:
   ```bash
   pytest --alluredir=allure-results
   ```
2. Generate the report:
   ```bash
   allure serve allure-results
   ```

## License
This project is licensed under the MIT License.
```