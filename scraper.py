import requests
from bs4 import BeautifulSoup

def search_amazon(product_name):
    search_url = f"https://www.amazon.com/s?k={product_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    prices = []
    for price_tag in soup.find_all('span', {'class': 'a-price-whole'}):
        price = price_tag.get_text()
        prices.append(float(price.replace(',', '')))

    if prices:
        return min(prices)
    else:
        return None
