# books_page.py
class BooksPage:
    BASE_BOOKS_URL = "https://www.amazon.com/books-used-books-textbooks/b/?ie=UTF8&node=283155&ref_=nav_cs_books_2ed85a0fb54a4598ba909c22690d166e"
    PAGE_TITLE = "Amazon.com: Books"
    BEST_BOOKS_BUTTON = "//a[@aria-label='Best books of the month']"
    CELEBRITY_PICKS_BUTTON = "//a[@aria-label='Celebrity Picks']"

    def __init__(self, page):
        self.page = page

    def navigate_to_books_page(self):
        self.page.goto(self.BASE_BOOKS_URL)

    def verify_books_page_title(self):
        actual_title = self.page.title()
        assert actual_title == self.PAGE_TITLE, f"Expected '{self.PAGE_TITLE}', but got '{actual_title}'"