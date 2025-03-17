import requests
from bs4 import BeautifulSoup

# URL of the e-commerce page
url = "https://example.com/products"

# Send request and get page content
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find all product elements
products = soup.find_all("div", class_="product-item")

# Extract product names & prices
for product in products:
    name = product.find("h2").text.strip()
    price = product.find("span", class_="price").text.strip()
    print(f"{name} - {price}")
