from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
books = soup.find_all("article", class_="product_pod")


data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]

    data.append({
        "Title": title,
        "Price": price,
        "Rating": rating
    })