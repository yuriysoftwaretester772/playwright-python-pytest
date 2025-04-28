import pytest
from playwright.sync_api import sync_playwright
import allure
from allure_commons.types import AttachmentType
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Change to DEBUG for more verbosity
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--custom-browser", action="store", default="chromium",
        help="Browser to run tests: chromium, firefox, or webkit"
    )
    parser.addoption(
        "--headless", action="store_true",
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="function")
def browser(request):
    logger.debug("Starting browser fixture setup")
    browser_name = request.config.getoption("--custom-browser").lower()
    headless = request.config.getoption("--headless")
    logger.debug(f"Browser: {browser_name}, Headless: {headless}")

    try:
        with sync_playwright() as p:
            if browser_name == "chromium":
                logger.debug("Launching Chromium browser")
                browser = p.chromium.launch(headless=headless)
            elif browser_name == "firefox":
                logger.debug("Launching Firefox browser (stable)")
                browser = p.firefox.launch(headless=headless, channel="firefox")
            elif browser_name == "msedge":
                logger.debug("Launching Microsoft Edge browser")
                browser = p.chromium.launch(headless=headless, channel="msedge")
            elif browser_name == "webkit":
                logger.debug("Launching WebKit browser")
                browser = p.webkit.launch(headless=headless)
            else:
                logger.error(f"Unsupported browser: {browser_name}")
                raise ValueError(f"Unsupported browser: {browser_name}")

            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                viewport={"width": 1920, "height": 1080}  # Set to full HD resolution
            )
            page = context.new_page()

            yield page

            logger.debug("Taking screenshot for Allure")
            try:
                allure.attach(
                    page.screenshot(),
                    name="Screenshot",
                    attachment_type=AttachmentType.PNG
                )
            except Exception as e:
                logger.warning(f"Failed to capture screenshot: {e}")

            logger.debug("Closing browser")
            browser.close()

    except Exception as e:
        logger.error(f"Failed to initialize browser: {e}")
        raise