import requests
from bs4 import BeautifulSoup
import os
url = 'https://ticket.com.tw/Application/UTK02/UTK0201_00.aspx?PRODUCT_ID=N0VQ76BZ'

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

# y = input('Please enter the year. eg:2021\n')
# m = input('Please enter the month. eg:03\n')
# d = input('Please enter the day. eg:28\n')
y = '2021'
m = '04'
d = '11'
tr = soup.find_all('tr')
for i in tr:
    l = i.find('time',{'datetime':y+'-'+m+'-'+d})
    if l != None:
        try:
            pur_url = 'https://ticket.com.tw/application/UTK02/'+i.find('button').get('onclick')[26:-1] 
            print('Get purchase website url.')
        print(pur_url)
        payload = {
            'PERFORMANCE_ID':'N0VTGV3K',
            'PRODUCT_ID': i.find('button').get('onclick')[75:-1]
        }
        print(payload)
        break
if l==None:
    print("[Error] Can't find the asking date information. Please check the format of the date is correct or not.")

r = requests.get(pur_url)
soup = BeautifulSoup(r.text,'html.parser')
chk_pic = soup.find('img',id = 'chk_pic')

link = 'https://ticket.com.tw/'+chk_pic.get("src")

if not os.path.exists('chk_pic'):
    os.makedirs('chk_pic')
img = requests.get(link)
with open('chk_pic\\'+'1.jpg','wb') as file:
    file.write(img.content)

chk = input()
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'ticket.com.tw',
    'Origin': 'https://ticket.com.tw',
    'Referer': pur_url,
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
with requests.Session() as s:
	payload_loginPage = {
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl00$H_NAME': '原價',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl00$H_PRICE': '300.0000',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl00$PRICE_TEXT': '300',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl00$AMOUNT': '1',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl01$H_PKNO': 'N0VTGVYB',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl01$H_NAME': '身心障礙者',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl01$H_PRICE': '150.0000',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl01$PRICE_TEXT': '150',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl01$AMOUNT': '0',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl02$H_NAME': '身障陪同者',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl02$H_PRICE': '150.0000',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl02$PRICE_TEXT': '150',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl02$AMOUNT':' 0',
        'ctl00$ContentPlaceHolder1$LOGIN_ID': 'A131892440',
        'ctl00$ContentPlaceHolder1$LOGIN_PWD': 'nono0627',
        'ctl00$ContentPlaceHolder1$CHK': chk,
        '__ASYNCPOST': 'true'
	}

	payload_loginPage["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
	payload_loginPage["__VIEWSTATEGENERATOR"] = soup.select_one("#__VIEWSTATEGENERATOR")["value"]
	payload_loginPage["__EVENTVALIDATION"] = soup.select_one("#__EVENTVALIDATION")["value"]
	s.post(pur_url, data=payload_loginPage, headers=headers)
 