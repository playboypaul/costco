import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://www.costco.com/whats-new.html"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

deals = []
for item in soup.select(".product"):
    title_tag = item.select_one(".product-title")
    price_tag = item.select_one(".price")
    link_tag = item.select_one("a")
    img_tag = item.select_one("img")
    if not (title_tag and price_tag and link_tag and img_tag):
        continue
    deals.append({
        "title": title_tag.text.strip(),
        "price": price_tag.text.strip(),
        "link": link_tag['href'],
        "img": img_tag['src']
    })

with open("../data/deals.json", "w") as f:
    json.dump({"date": str(datetime.now()), "deals": deals}, f, indent=2)
print(f"Scraped {len(deals)} deals")
