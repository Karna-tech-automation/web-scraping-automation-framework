from scraper.book_scraper import BookScraper
from utils.csv_writer import save_to_csv


def main():

    scraper = BookScraper()

    scraper.open_site()

    books = scraper.scrape_books()

    save_to_csv(books, "output/books.csv")

    scraper.close()

    print("Scraping finished")


if __name__ == "__main__":
    main()