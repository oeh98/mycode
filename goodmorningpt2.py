#!/usr/bin/env python3
#import request libary, allows sending of http extremley easy without manually writing query strings to urls

import requests
import schedule
import time

def send_reminder():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '5098408197',
        'message': 'Your survey is due in an hour',
        'key': 'textbelt_test',
    })
    print(resp.json())

#schedule.every().friday.at("15:00").do(send_reminder)
#schedule.every().day.at("14:09").do(send_reminder)
schedule.every(schedule.every(10).minutes.do).minutes.do(send_reminder)
# Loop so that the scheduling task
# keeps on running all time.
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
