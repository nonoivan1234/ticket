import requests
from bs4 import BeautifulSoup
params = {
"id": "1307452782694451",
"ev": "SubscribedButtonClick",
"dl": "https://ticket.com.tw/Application/UTK02/UTK0202_.aspx?PERFORMANCE_ID=N0VTGV3K&PRODUCT_ID=N0VQ76BZ",
"rl": "https://ticket.com.tw/Application/UTK02/UTK0201_00.aspx?PRODUCT_ID=N0VQ76BZ",
"if": "false",
"ts": "1616725985894",
"cd[buttonFeatures]": '{"classList":"btn-group bootstrap-select open","destination":"https://ticket.com.tw/Application/UTK02/UTK0202_.aspx?PERFORMANCE_ID=N0VTGV3K&PRODUCT_ID=N0VQ76BZ","id":"","imageUrl":"","innerText":"-請選擇-\n \n-請選擇-\n1F自由入座 300\n2F自由入座 200\n-請選擇-\n1F自由入座 300\n2F自由入座 200","numChildButtons":4,"tag":"div"}',
"cd[buttonText]": "-請選擇- -請選擇-0F自由入座 00F自由入座 0-請選擇-0F自由入座 00F自由入座 0",
"cd[formFeatures]": '[{"id":"__EVENTTARGET","name":"__EVENTTARGET","tag":"input","inputType":"hidden","valueMeaning":"empty"},{"id":"__EVENTARGUMENT","name":"__EVENTARGUMENT","tag":"input","inputType":"hidden","valueMeaning":"empty"},{"id":"__LASTFOCUS","name":"__LASTFOCUS","tag":"input","inputType":"hidden","valueMeaning":"empty"},{"id":"__VIEWSTATE","name":"__VIEWSTATE","tag":"input","inputType":"hidden"},{"id":"__VIEWSTATEGENERATOR","name":"__VIEWSTATEGENERATOR","tag":"input","inputType":"hidden"},{"id":"__EVENTVALIDATION","name":"__EVENTVALIDATION","tag":"input","inputType":"hidden"},{"id":"mainMenu","name":"","tag":"button"},{"id":"searchBtn","name":"","tag":"button"},{"id":"","name":"","tag":"button"},{"id":"searchInput","name":"","tag":"input","placeholder":"請輸入欲搜尋關鍵字","inputType":"text","valueMeaning":"empty"},{"id":"ctl00_MASTER_S_ORDER_DATE","name":"ctl00$MASTER_S_ORDER_DATE","tag":"input","inputType":"hidden","valueMeaning":"empty"},{"id":"ctl00_MASTER_E_ORDER_DATE","name":"ctl00$MASTER_E_ORDER_DATE","tag":"input","inputType":"hidden","valueMeaning":"empty"},{"id":"ctl00_MASTER_ddlPG","name":"ctl00$MASTER_ddlPG","tag":"select","valueMeaning":"empty"},{"id":"ctl00_MASTER_ddlSelArea","name":"ctl00$MASTER_ddlSelArea","tag":"select","valueMeaning":"empty"},{"id":"MASTER_btnSearch_Submit","name":"","tag":"button"},{"id":"ctl00_ContentPlaceHolder1_PERFORMANCE_ID","name":"ctl00$ContentPlaceHolder1$PERFORMANCE_ID","tag":"input","inputType":"hidden"},{"id":"ctl00_ContentPlaceHolder1_PRODUCT_ID","name":"ctl00$ContentPlaceHolder1$PRODUCT_ID","tag":"input","inputType":"hidden"},{"id":"ctl00_ContentPlaceHolder1_PLACE_ID","name":"ctl00$ContentPlaceHolder1$PLACE_ID","tag":"input","inputType":"hidden"},{"id":"ctl00_ContentPlaceHolder1_PRODUCT_CATEGORY_ID","name":"ctl00$ContentPlaceHolder1$PRODUCT_CATEGORY_ID","tag":"input","inputType":"hidden"},{"id":"ctl00_ContentPlaceHolder1_SHOW_PLACE_MAP","name":"ctl00$ContentPlaceHolder1$SHOW_PLACE_MAP","tag":"input","inputType":"hidden","valueMeaning":"empty"},{"id":"ctl00_ContentPlaceHolder1_PERFORMANCE_PRICE_AREA_ID","name":"ctl00$ContentPlaceHolder1$PERFORMANCE_PRICE_AREA_ID","tag":"input","inputType":"hidden","valueMeaning":"empty"},{"id":"ctl00_ContentPlaceHolder1_PACKAGE_ID","name":"ctl00$ContentPlaceHolder1$PACKAGE_ID","tag":"input","inputType":"hidden","valueMeaning":"empty"},{"id":"","name":"","tag":"button"},{"id":"ctl00_ContentPlaceHolder1_PRICE","name":"ctl00$ContentPlaceHolder1$PRICE","tag":"select"},{"id":"ctl00_ContentPlaceHolder1_CHK","name":"ctl00$ContentPlaceHolder1$CHK","tag":"input","placeholder":"請輸入圖片上符號","inputType":"text","valueMeaning":"empty"},{"id":"ctl00_ContentPlaceHolder1_AddShopingCart","name":"ctl00$ContentPlaceHolder1$AddShopingCart","tag":"input","inputType":"submit"},{"id":"myInput","name":"","tag":"button"}]',
"cd[pageFeatures]": {"title":"\n\t\n    年代售票 | 2020-2021年第18屆SBL 超級籃球聯賽 | 選擇座位/數量\n\n"},
"cd[parameters]": "[]",
'sw': '1536',
'sh': '864',
'v': '2.9.33',
'r': 'stable',
'ec': '3',
'o': '1054',
'fbp': 'fb.2.1616725532391.1801478835',
'it': '1616725900004',
'coo': 'false',
'es': 'automatic',
'tm': '3',
'rqm': 'formPOST'
}
url = 'https://ticket.com.tw/Application/UTK02/UTK0201_.aspx?PRODUCT_ID=N0VQ76BZ'

r = requests.post(url, params = params)