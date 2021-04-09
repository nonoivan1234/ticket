import requests
from bs4 import BeautifulSoup

url = 'https://ticket.com.tw/Application/UTK02/UTK0201_00.aspx?PRODUCT_ID=N0VQ76BZ'

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

# y = input('Please enter the year. eg:2021\n')
# m = input('Please enter the month. eg:03\n')
# d = input('Please enter the day. eg:28\n')
y = '2021'
m = '04'
d = '10'
tr = soup.find_all('tr')
for i in tr:
    l = i.find('time',{'datetime':y+'-'+m+'-'+d})
    if l != None:
        print('Get purchase website url.')
        pur_url = 'https://ticket.com.tw/application/UTK02/'+i.find('button').get('onclick')[26:-1]
        print(pur_url)
        payload = {
            'PERFORMANCE_ID':'N0VTGV3K',
            'PRODUCT_ID': i.find('button').get('onclick')[75:-1]
        }
        print(payload)
        break
if l==None:
    print("[Error] Can't find the asking date information. Please check the format of the date is correct or not.")