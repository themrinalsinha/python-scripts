#!/usr/bin/python3
# Author : Mrinal Sinha

"""
Using coindesk API to find the current price of Bitcoin This is written 
to display current rate in INR (Indian Rupee) other supported currencies
https://api.coindesk.com/v1/bpi/supported-currencies.json
"""

from requests       import Session
from fake_useragent import UserAgent

session     = Session()
bitcoin_api = 'https://api.coindesk.com/v1/bpi/currentprice/INR.json'
fake_header = {'User-Agent' : str(UserAgent().Chrome)}
response    = session.get(bitcoin_api, headers=fake_header).json()

rate_inr = response['bpi']['INR']['rate']
rate_usd = response['bpi']['USD']['rate']
update_t = response['time']['updated']

print('Updated time: {}\nRate in INR : ₹ {}\nRate in USD : $ {}'\
                            .format(update_t, rate_inr, rate_usd))

