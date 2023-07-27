#web3.py
from bs4 import BeautifulSoup
import requests

URL = "https://www.naver.com"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup) 