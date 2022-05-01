import requests
from bs4 import BeautifulSoup

url = 'https://www.mirea.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('div', class_='bonus_cart-title')

for quote in quotes:
    data = quote.text

