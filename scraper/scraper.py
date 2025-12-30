from bs4 import BeautifulSoup
import requests
import pandas as pd

class Scraper:
    def __init__(self, url):
        self.url = url
        self.data = []

    def fetch_page(self):
        response = requests.get(self.url)
        response.raise_for_status()            # If something goes wrong (404, no internet etc.), stop and show an error
        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]
            self.data.append({ "Title": title, "Price": price, "Rating": rating })

    
    def to_dataframe(self):
        return pd.DataFrame(self.data)
    
    def save_csv(self, filename):
        df = self.to_dataframe()
        df.to_csv(filename, index=False)

        

