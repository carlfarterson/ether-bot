# Sends alert if USDT is moved from the primary holding account.
# There may be some positive correlation w/ USDT printed & BTC price
import pandas as pd
import pytz
import telegram
import requests

from datetime import datetime

from selenium import webdriver


url = 'https://www.omniexplorer.info/address/1NTMakcgVwQpMdGxRQnFKyb3G1FAJysSfz'

driver = webdriver.



def find_amt_date(element):
    row = element.text.split('\n')
    amt = row[1]
    date = row[4]
    date = datetime.strptime(date, '%m/%d/%Y %H:%M:%S %p')
    utc_date = pytz.timezone('UTC').localize(date, is_dst=None)
    utc_date_str = datetime.strftime(date, '%m/%d/%Y %H:%M:%S %p (UTC)')
    return amt, utc_date_str

def run(chrome):
    prev_amt = pd.read_csv('tether.csv'').iloc[0, 0]
    chrome.get(url)
    table  = chrome.load('ul[@class="result-list"]/div/div[1]')

    for element in table:
        amt, date = find_amt_date(element)
        if amt == prev_amt:
            break

        message = 'ALERT: ' + amt + ' USDT sent on ' + date
        telegram.send_message(file=__file__, message=message)

    most_recent_amt, _ = find_amt_date(table[0])
    pd.DataFrame(data=[most_recent_amt], columns=['Tether Printed']).to_csv(CSV_FILE,index=False)
