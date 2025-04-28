# search_result_page.py
from .base_page import AmazonBasePage

class AmazonSearchResultPage(AmazonBasePage):
    PAGE_TITLE = "Amazon.com : "

    def verify_title(self, item: str):
        self.page.wait_for_load_state("domcontentloaded")
        actual_title = self.page.title()
        assert item.lower() in actual_title.lower(), f"Expected '{item}' in title, but got '{actual_title}'"