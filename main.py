from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import requests
from bs4 import BeautifulSoup
import os

# clear the input box and send the value
def input_(element_name, to_enter):
    element_name.clear()
    element_name.send_keys(to_enter)
    

# get chk_pic and return driver
def get_chk_pic(y, m, d): 
    
    # find the buting ticket website start
    url = 'https://ticket.com.tw/application/UTK02/UTK0201_00.aspx?PRODUCT_ID=N0VQ76BZ'

    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')

    tr = soup.find_all('tr')
    for sub in tr:
        temp = sub.find('time',{'datetime' : y+'-'+m+'-'+d})
        if temp != None:
            try:    
                pur_url = 'https://ticket.com.tw/application/UTK02/'+sub.find('button').get('onclick')[26:-1]        
                print('Get purchase website url.')
                break
            except :
                print("[ERROR] Can't buy the asking date's ticket.")
                quit()
    else:
        print("[ERROR] Can't find the asking date data.")
        quit()

    # open the buying ticket website
    options = Options()
    options.add_argument("--disable-notifications")
    chrome = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
    chrome.get(pur_url)

    # check picture download
    if not os.path.exists('chk_pic'):
        os.makedirs('chk_pic')
    with open('chk_pic\\'+'chk.jpg','wb') as file:
        l = chrome.find_element_by_xpath('//*[@id="chk_pic"]')
        file.write(l.screenshot_as_png)
        
    chrome.minimize_window()
    return chrome 


# user input the chk num by identify the chk_pic
def ticket_buying(driver, ID, password_str, original, disabilities, with_disabilities, chk): 

    # select the seat option
    select = Select(driver.find_element_by_name("ctl00$ContentPlaceHolder1$PRICE"))
    select.select_by_index(0)

    # find every element
    original_ticket = driver.find_element_by_id("ctl00_ContentPlaceHolder1_PriceTypeList_ctl00_AMOUNT")
    disabilities_ticket = driver.find_element_by_id("ctl00_ContentPlaceHolder1_PriceTypeList_ctl01_AMOUNT")
    with_disabilities_ticket = driver.find_element_by_id('ctl00_ContentPlaceHolder1_PriceTypeList_ctl02_AMOUNT')


    chk_ = driver.find_element_by_id("ctl00_ContentPlaceHolder1_CHK")
    identify = driver.find_element_by_id("ctl00_ContentPlaceHolder1_LOGIN_ID")
    password = driver.find_element_by_name("ctl00$ContentPlaceHolder1$LOGIN_PWD")
    btn = driver.find_element_by_name("ctl00$ContentPlaceHolder1$AddShopingCart")

    # input and send the information
    input_(original_ticket, original)
    input_(disabilities_ticket, disabilities)
    input_(with_disabilities_ticket, with_disabilities)
    input_(chk_, chk)
    input_(identify, ID)
    input_(password, password_str)
    btn.click()
    
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    chk_window = soup.find(class_='ui-dialog-content ui-widget-content')
    btn_chk = driver.find_element_by_class_name('ui-dialog-buttonset').find_element_by_tag_name('button')
    
    # check purchase successful or not
    if chk_window.text == '加入購物車完成, 請於 10 分鐘內完成結帳!':
        print('[COOL] Purchase successful')
        btn_chk.click()
        driver.maximize_window()
        return True
    
    else :
        print('[ERROR] Failed to purchase please check the data.')
        btn_chk.click()
        time.sleep(1)
        
        # redownload the chk_pic
        with open('chk_pic\\'+'chk.jpg','wb') as file:
            l = driver.find_element_by_xpath('//*[@id="chk_pic"]')
            file.write(l.screenshot_as_png)
            
        driver.minimize_window()
        return False