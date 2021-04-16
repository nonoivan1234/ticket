from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import requests
from bs4 import BeautifulSoup
import os
 
def input_ticket(element_name, to_enter):
    element_name.clear()
    element_name.send_keys(to_enter)
    
url = 'https://ticket.com.tw/application/UTK02/UTK0201_00.aspx?PRODUCT_ID=N0VQ76BZ'

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

y = input('Please enter the year. eg:2021\n')
m = input('Please enter the month. eg:03\n')
d = input('Please enter the day. eg:28\n')
# y = '2021'
# m = '04'
# d = '23'
tr = soup.find_all('tr')
for i in tr:
    l = i.find('time',{'datetime' : y+'-'+m+'-'+d})
    if l != None:
        try:    
            pur_url = 'https://ticket.com.tw/application/UTK02/'+i.find('button').get('onclick')[26:-1]        
            print('Get purchase website url.')
            break
        except :
            print("[ERROR] Could not find the asking date data.")
            quit()

 
options = Options()
options.add_argument("--disable-notifications")
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get(pur_url)

select = Select(chrome.find_element_by_name("ctl00$ContentPlaceHolder1$PRICE"))
select.select_by_index(0)

original_ticket = chrome.find_element_by_id("ctl00_ContentPlaceHolder1_PriceTypeList_ctl00_AMOUNT")
disabilities_ticket = chrome.find_element_by_id("ctl00_ContentPlaceHolder1_PriceTypeList_ctl01_AMOUNT")
with_disabilities_ticket = chrome.find_element_by_id('ctl00_ContentPlaceHolder1_PriceTypeList_ctl02_AMOUNT')
original = input("請輸入原價票數 票價：200\n")
disabilities = input("請輸入身心障礙者票數 票價：100\n")
with_disabilities = input("請輸入身障陪同者票數 票價：100\n")
chk_pic = chrome.find_element_by_id("ctl00_ContentPlaceHolder1_CHK")
identify = chrome.find_element_by_id("ctl00_ContentPlaceHolder1_LOGIN_ID")
password = chrome.find_element_by_name("ctl00$ContentPlaceHolder1$LOGIN_PWD")
btn = chrome.find_element_by_name("ctl00$ContentPlaceHolder1$AddShopingCart")
chk = input("請輸入驗證碼\n")
input_ticket(original_ticket, original)
input_ticket(disabilities_ticket, disabilities)
input_ticket(with_disabilities_ticket, with_disabilities)
chk_pic.send_keys(chk)
identify.send_keys('A131892440')
password.send_keys('nono0627')
btn.click()

time.sleep(15)