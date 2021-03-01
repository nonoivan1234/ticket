import requests
from bs4 import BeautifulSoup


url = "https://www.thsrc.com.tw/ArticleContent/a3b630bb-1066-4352-a1ef-58c7b4e8ef7c?search=f03JL80+mmAuu/IkmM0KUfOVuVgoIcBklIxs89NGvo1Et/ri48Yxj4ZQopwa+wqwDi8PS0KxNMhkikGDM0+U8EFSlocCthrGLzKkleMaPKwiHa7UNHPEQ3ZjXZrLOTd6B52LDLUfu0a/DdkGpG43hdPY76xx+mPmWfPKW5NHRgM1CRa9s0ld6XsxKfDCqnHOV5zLzD1wxFOWPfBzXvn62g=="

payload = {
    'SearchType':5,
    'Lang':'TW',
    'StartStation':'NanGang',
    'EndStation':'ZuoYing',
    'OutWardSearchDate': '2021/03/02',
    'OutWardSearchTime': '05:00',
    'ReturnSearchDate': '2021/03/02',
    'ReturnSearchTime': '05:00',
    'DiscountType':''
}
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')


print(r.text)