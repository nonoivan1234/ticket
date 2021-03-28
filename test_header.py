import requests
from bs4 import BeautifulSoup
import os

url = 'https://ticket.com.tw/Application/UTK02/UTK0202_.aspx?PERFORMANCE_ID=N0VTGVMM&PRODUCT_ID=N0VQ76BZ'
r = requests.get(url)
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
    'Referer': 'https://ticket.com.tw/application/UTK02/UTK0202_.aspx?PERFORMANCE_ID=N0VTGVMM&PRODUCT_ID=N0VQ76BZ',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
with requests.Session() as s:
	page = s.post('https://ticket.com.tw/application/UTK02/UTK0202_.aspx?PERFORMANCE_ID=N0VTGVMM&PRODUCT_ID=N0VQ76BZ', headers = headers)
	soup = BeautifulSoup(page.content, 'html.parser')

	payload_loginPage = {
        'ctl00$ScriptManager1': 'ctl00$ContentPlaceHolder1$AjaxPanel|ctl00$ContentPlaceHolder1$AddShopingCart',
        'ctl00$MASTER_S_ORDER_DATE':'' ,
        'ctl00$MASTER_E_ORDER_DATE': '',
        'ctl00$MASTER_ddlPG': '',
        'ctl00$MASTER_ddlSelArea': '',
        'ctl00$ContentPlaceHolder1$PERFORMANCE_ID': 'N0VTGVMM',
        'ctl00$ContentPlaceHolder1$PRODUCT_ID': 'N0VQ76BZ',
        'ctl00$ContentPlaceHolder1$PLACE_ID': 'N07Y9GZN',
        'ctl00$ContentPlaceHolder1$PRODUCT_CATEGORY_ID': '218',
        'ctl00$ContentPlaceHolder1$SHOW_PLACE_MAP':'' ,
        'ctl00$ContentPlaceHolder1$PERFORMANCE_PRICE_AREA_ID':'' ,
        'ctl00$ContentPlaceHolder1$PACKAGE_ID':'' ,
        'ctl00$ContentPlaceHolder1$ACTIVITY_GROUP_ID':'' ,
        'ctl00$ContentPlaceHolder1$ACTIVITY_GROUP_ITEM_ID':'' ,
        'ctl00$ContentPlaceHolder1$QUANTITY_LIMIT': '0',
        'ctl00$ContentPlaceHolder1$IS_NONSEAT_USE_SERIALNO': 'N',
        'ctl00$ContentPlaceHolder1$DOC_MEMO': '{"N0VTGVYD":"aiLHFRChOB2bSmSVe4B/qf4/iVZ86E51bZ57lZdODI6zqoCOsyjKVC8ZigqOJisD6QjyudW5tnc=","N0VTGVYU":"PXLHiophn10cjpNHN/CCDHIQm4TFqgDmg2BhhNgPQ9enc7OnZG7cta6Z+w0sFocLCBQUDGk2HVI=","N0VTGVYB":"aiLHFRChOB2bSmSVe4B/qf4/iVZ86E51bZ57lZdODI6zqoCOsyjKVC8ZigqOJisD6QjyudW5tnc="}',
        'ctl00$ContentPlaceHolder1$ORGANIZATION_ID': 'N0176158',
        'ctl00$ContentPlaceHolder1$PRICE': 'N0VTGVY4|1699',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl00$H_PKNO': 'N0VTGVYU',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl00$H_NAME': '原價',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl00$H_PRICE': '300.0000',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl00$PRICE_TEXT': '300',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl00$AMOUNT': '1',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl01$H_PKNO': 'N0VTGVYB',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl01$H_NAME': '身心障礙者',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl01$H_PRICE': '150.0000',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl01$PRICE_TEXT': '150',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl01$AMOUNT': '0',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl02$H_PKNO': 'N0VTGVYD',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl02$H_NAME': '身障陪同者',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl02$H_PRICE': '150.0000',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl02$PRICE_TEXT': '150',
        'ctl00$ContentPlaceHolder1$PriceTypeList$ctl02$AMOUNT':' 0',
        'ctl00$ContentPlaceHolder1$LOGIN_ID': 'A131892440',
        'ctl00$ContentPlaceHolder1$LOGIN_PWD': 'nono0627',
        'ctl00$ContentPlaceHolder1$CHK': chk,
        'ctl00$ContentPlaceHolder1$AddShopingCart': '加入購物車，下一步',
        '__ASYNCPOST': 'true',
        '__EVENTTARGET':'', 
        '__EVENTARGUMENT':'', 
        '__LASTFOCUS':''
	}

	payload_loginPage["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
	payload_loginPage["__VIEWSTATEGENERATOR"] = soup.select_one("#__VIEWSTATEGENERATOR")["value"]
	payload_loginPage["__EVENTVALIDATION"] = soup.select_one("#__EVENTVALIDATION")["value"]
	s.post('https://ticket.com.tw/Application/UTK02/UTK0202_.aspx', data=payload_loginPage, headers=headers)
 
print(soup.prettify())