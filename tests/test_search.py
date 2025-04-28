import pytest
from pages.home_page import AmazonHomePage
from pages.search_result_page import AmazonSearchResultPage

@pytest.mark.regressiontest
def test_search_airmax(browser):
    home_page = AmazonHomePage(browser)
    search_result_page = AmazonSearchResultPage(browser)
    search_item = 'nike air max'

    # Navigate to Amazon.com home page
    home_page.load_page()

    # Verify that web page title is Amazon.com
    home_page.verify_title()

    # Search for Nike Air Max
    home_page.search_item(search_item)

    # Verify that web page title contains Nike Air Max
    search_result_page.verify_title(search_item)