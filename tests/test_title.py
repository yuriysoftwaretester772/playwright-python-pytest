import pytest
from pages.home_page import AmazonHomePage

@pytest.mark.smoketest
def test_amazon_title(browser):
    home_page = AmazonHomePage(browser)

    # Navigate to Amazon home page
    home_page.load_page()

    # Verify Amazon home page title matches the expected title
    home_page.verify_title()