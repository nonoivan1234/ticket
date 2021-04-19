import main

dates_locations_prices_webs = main.get_status()
print(dates_locations_prices_webs)
n = int(input())

url = 'https://ticket.com.tw/application/UTK02/' + dates_locations_prices_webs[3][n]
driver = main.get_chk_pic(url)

# chk = input()

# # loop for fail purchase until success by retry the chk_pic
# while not main.ticket_buying(driver, 'A131892440', 'nono0627', '1', '0', '0', chk):
#     chk = input()
#     main.ticket_buying(driver, 'A131892440', 'nono0627', '1', '0', '0', chk)