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
    

# get game status and return array includes dates, locations, prices, webs wach of the element is a array
def get_status(): 
    dates_locations_prices_webs = [[] for i in range (4)]
    # find the buting ticket website start
    url = 'https://ticket.com.tw/application/UTK02/UTK0201_00.aspx?PRODUCT_ID=N0VQ76BZ'

    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    temp = 0
    tr = soup.find_all('tr')
    for sub in tr:
        
        if sub.find('time', {'class' : 'icon'}) != None:
            dates_locations_prices_webs[0].append(sub.find('time', {'class' : 'icon'}).get('datetime'))
            
        if sub.find('span', {'id' : 'ctl00_ContentPlaceHolder1_PerformanceList_ctl0'+str(temp)+'_PLACE_NAME'}) != None:
            dates_locations_prices_webs[1].append(sub.find('span', {'id' : 'ctl00_ContentPlaceHolder1_PerformanceList_ctl0'+str(temp)+'_PLACE_NAME'}).getText())
            
        if sub.find('span', {'id' : 'ctl00_ContentPlaceHolder1_PerformanceList_ctl0'+str(temp)+'_Label1'}) != None:
            dates_locations_prices_webs[2].append(sub.find('span', {'id' : 'ctl00_ContentPlaceHolder1_PerformanceList_ctl0'+str(temp)+'_Label1'}).getText())
            
        if sub.find('button', {'class' : 'btn btn-event'}) != None:
            dates_locations_prices_webs[3].append(sub.find('button', {'class' : 'btn btn-event'}).get('onclick')[26:-1])
            temp += 1
    
    return dates_locations_prices_webs


# get chk_pic and return driver    
def get_chk_pic(pur_url):
    # open the buying ticket website
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
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