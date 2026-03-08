from selenium.webdriver.common.by import By
from scraper.driver_factory import get_driver
from config import BASE_URL, MAX_PAGES
from utils.logger import get_logger
from tenacity import retry, stop_after_attempt, wait_fixed


class BookScraper:

    def __init__(self):

        self.driver = get_driver()
        self.logger = get_logger()

    def open_site(self):

        self.driver.get(BASE_URL)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def scrape_books(self):

        all_books = []

        for page in range(1, MAX_PAGES + 1):

            self.logger.info(f"Scraping page {page}")

            books = self.driver.find_elements(By.CLASS_NAME, "product_pod")

            for book in books:

                title = book.find_element(By.TAG_NAME, "h3").text
                price = book.find_element(By.CLASS_NAME, "price_color").text

                all_books.append({
                    "title": title,
                    "price": price
                })

            try:
                next_button = self.driver.find_element(By.CLASS_NAME, "next")
                next_button.click()
            except:
                break

        return all_books

    def close(self):

        self.driver.quit()