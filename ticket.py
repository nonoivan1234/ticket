import requests
from bs4 import BeautifulSoup

url = 'https://ticket.com.tw/Application/UTK02/UTK0201_.aspx?PRODUCT_ID=N0VQ76BZ'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())