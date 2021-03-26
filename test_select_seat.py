import requests
from bs4 import BeautifulSoup
import os

url = 'https://ticket.com.tw/Application/UTK02/UTK0202_.aspx?PERFORMANCE_ID=N0VTGVMM&PRODUCT_ID=N0VQ76BZ'

headers = {
    'access-control-allow-credentials': 'true',
    'access-control-allow-origin': 'https://ticket.com.tw',
    'alt-svc': 'h3-29=":443"; ma=3600,h3-27=":443"; ma=3600',
    'content-length': '0',
    'content-type': 'text/plain',
    'cross-origin-resource-policy': 'cross-origin',
    'date': 'Fri, 26 Mar 2021 14:41:29 GMT',
    'priority': 'u=3,i',
    'server': 'proxygen-bolt',
    'strict-transport-security': 'max-age=31536000; includeSubDomains'
}
r = requests.post(url,headers = headers)
soup = BeautifulSoup(r.text,'lxml')
pic = soup.find('img',id = 'chk_pic')
print(r.text)
link = 'https://ticket.com.tw/'+pic.get("src")


if not os.path.exists('chk_pic'):
    os.makedirs('chk_pic')
img = requests.get(link)
with open('chk_pic\\'+'1.jpg','wb') as file:
    file.write(img.content)