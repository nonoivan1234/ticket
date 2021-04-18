import final

driver = final.get_chk_pic('2021', '05', '23')
chk = input()

# loop for fail purchase until success by retry the chk_pic
while not final.ticket_buying(driver, 'A131892440', 'nono0627', '1', '0', '0', chk):
    chk = input()
    final.ticket_buying(driver, 'A131892440', 'nono0627', '1', '0', '0', chk)