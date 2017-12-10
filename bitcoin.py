#!/usr/bin/python3
# Author : Mrinal Sinha

"""
Using coindesk API to find the current price of Bitcoin This is written 
to display current rate in INR (Indian Rupee) other supported currencies
https://api.coindesk.com/v1/bpi/supported-currencies.json
"""

import notify2
from time           import sleep
from os.path        import realpath, dirname
from requests       import Session
from subprocess     import check_call
from fake_useragent import UserAgent

BITCOIN_IMAGE   = dirname(realpath(__file__)) + '/bitcoin.png'

def get_update():
    session     = Session()
    bitcoin_api = 'https://api.coindesk.com/v1/bpi/currentprice/INR.json'
    fake_header = {'User-Agent' : str(UserAgent().Chrome)}
    return session.get(bitcoin_api, headers=fake_header).json()

cur_rate = 0
while True:
    try:
        response = get_update()
    except: pass
    rate_inr = response['bpi']['INR']['rate']
    rate_usd = response['bpi']['USD']['rate']
    update_t = response['time']['updated']

    if cur_rate != rate_inr:
        cur_rate = rate_inr

        notify2.init('BITCOIN RATE')
        notify = notify2.Notification(
            'BITCOIN RATE',
            'UPDATED : {}\nINR : ₹ {}\nUSD : $ {}'.format(update_t, rate_inr, rate_usd),
            icon = BITCOIN_IMAGE
        ).show()
        current_price = float(''.join(x for x in cur_rate.split(',')))
        check_call(['spd-say', 'Price changed to rupees {}'.format(current_price)])
        print('\rUpdated time: {}\nRate in INR : ₹ {}\nRate in USD : $ {}'\
                            .format(update_t, rate_inr, rate_usd), end = '')

        # Refresh rate to 1 second.
        sleep(1)