#web2.py
import requests

from bs4 import BeautifulSoup

url = "https://www.daangn.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    title = post.find("h2", attrs={"class":"card-title"})
    price = post.find("div",attrs={"class":"card-price"})
    addr = post.find("div", attrs={"class":"card-region-name"})
    print("{0},{1},{2}".format(title.text, price.text, addr.text))
