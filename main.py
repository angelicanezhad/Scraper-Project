from scraper.scraper import Scraper

URL = "https://books.toscrape.com/"

scraper = Scraper(URL)
html = scraper.fetch_page()
scraper.parse(html)

print(len(scraper.data))  # DEBUG LINE

scraper.save_csv("data/books.csv")

print("Scraping complete. Data saved.")