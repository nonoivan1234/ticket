import requests
from bs4 import BeautifulSoup

url = 'https://ticket.com.tw/Application/UTK02/UTK0202_.aspx?PERFORMANCE_ID=N0VTGVMM&PRODUCT_ID=N0VQ76BZ'
headers = {
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cache-control': 'max-age=0',
    # 'content-length': '6801',
    # 'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'fr=0DYI8XEt2I33me1rX..BgXo5h...1.0.BgXo5h.',
    # 'origin': 'https://ticket.com.tw',
    # 'referer': 'https://ticket.com.tw/',
    # 'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-fetch-dest': 'iframe',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'cross-site',
    # 'sec-fetch-user': '?1',
    # 'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
r = requests.post(url,headers = headers)
print(r)