import requests
from bs4 import BeautifulSoup
import os

def get_hotdeal(item):
    
    url = "https://slickdeals.net/newsearch.php?src=SearchBar&pp=20&forum_id=Array&price_range=Array&previous_days=0&q={}&r=1".format(item)

    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    rows = bs.select("div.resultRow")

    results = []

    for r in rows:
        link = r.select("a.dealTitle")[0]
        
        title = link.text
        href = link.get("href")
        
        if href is None:
            continue
        
        href = "https://slickdeals.net" + href

        price = r.select("span.price")[0].text.replace("$", "").replace("from", "").replace("Free","").strip()
        
        if price.find("/") >= 0 or price == "":
            continue

        hot = len(r.select("span.icon-fire"))

        results.append((title, href, price, hot))
    
    return results

os.system("cls")

print("Hi there! I'll find hot deals you want")
item = input("Can you tell me what you want?")

print(get_hotdeal(item))
print("Here they are!")
    