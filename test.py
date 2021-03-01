import requests
import pandas as pd

url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime'

payload = {
    "_csrf":"1cc42578-c333-4b96-bf2f-cda16eeefb91","startStation":"1000-臺北","endStation":"0960-汐止","transfer":"ONE","rideDate":"2021/03/02","startOrEndTime":"true","startTime":"00:00","endTime":"23:59","trainTypeList":"ALL","_isQryEarlyBirdTrn":"on","query":"查詢"
}

r = requests.post(url,data=payload)

table = pd.read_html(r.text)

for i in range (1,len(table)):
    string = str(table[i])
    ind = string.index('0')
    ind_end = string.index("。")
    print(string[ind+2:ind_end])