# home_page.py
from .base_page import AmazonBasePage

class AmazonHomePage(AmazonBasePage):
    URL = "https://www.amazon.com"
    PAGE_TITLE = "Amazon.com"

    def load_page(self):
        self.page.goto(self.URL)
        self.page.wait_for_selector(self.SEARCH_FIELD)

    def verify_title(self):
        actual_title = self.page.title()
        assert self.PAGE_TITLE in actual_title, f"Expected '{self.PAGE_TITLE}' in title, but got '{actual_title}'"