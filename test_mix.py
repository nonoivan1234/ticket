import requests
from bs4 import BeautifulSoup
import os

url = 'https://ticket.com.tw/application/UTK02/UTK0201_00.aspx?PRODUCT_ID=N0VQ76BZ'

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

# y = input('Please enter the year. eg:2021\n')
# m = input('Please enter the month. eg:03\n')
# d = input('Please enter the day. eg:28\n')
y = '2021'
m = '03'
d = '31'
tr = soup.find_all('tr')
for i in tr:
    l = i.find('time',{'datetime':y+'-'+m+'-'+d})
    if l != None:
        print('Get purchase website url.')
        pur_url = 'https://ticket.com.tw/application/UTK02/'+i.find('button').get('onclick')[26:-1]        
        break
if l==None:
    print("[Error] Can't find the asking date information. Please check the format of the date is correct or not.")

r = requests.get(pur_url)
soup = BeautifulSoup(r.text,'lxml')
chk_pic = soup.find('img',id = 'chk_pic')

link = 'https://ticket.com.tw/'+chk_pic.get("src")

if not os.path.exists('chk_pic'):
    os.makedirs('chk_pic')
img = requests.get(link)
with open('chk_pic\\'+'1.jpg','wb') as file:
    file.write(img.content)