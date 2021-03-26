import requests
from bs4 import BeautifulSoup
import os

url = 'https://ticket.com.tw/Application/UTK02/UTK0202_.aspx?PERFORMANCE_ID=N0VTGV3K&PRODUCT_ID=N0VQ76BZ#'

r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
pic = soup.find('img',id = 'chk_pic')

link = 'https://ticket.com.tw/'+pic.get("src")
print(link)

if not os.path.exists('chk_pic'):
    os.makedirs('chk_pic')
img = requests.get(link)
with open('chk_pic\\'+'1.jpg','wb') as file:
    file.write(img.content)