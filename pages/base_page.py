# base_page.py
from playwright.sync_api import Page
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class AmazonBasePage:
    SEARCH_FIELD = "#twotabsearchtextbox"

    def __init__(self, page: Page):
        self.page = page

    def search_item(self, item: str):
        try:
            self.page.fill(self.SEARCH_FIELD, item)
            self.page.press(self.SEARCH_FIELD, "Enter")
        except Exception as e:
            logger.error(f"Failed to search for '{item}': {e}")
            raise