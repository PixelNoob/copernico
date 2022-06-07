from binance.client import Client
import json
from datetime import datetime, timedelta, time
import time
import schedule

#apì keys
api_key= ''
api_secret= ''
client = Client(api_key, api_secret)

# Symbol you wish to trade and price
symbol = 'BNBUSDT'
price = client.get_avg_price(symbol=symbol)

# initialize bot lol
print('Copernico TWAP BOT initializing...')
time.sleep(1)
print('{} Price: {}'.format(symbol, price['price']))

## TWAP BUY
# HOW MUCH OF THE ASSET YOU WISH TO BUY
quantity = 0.04
def job():
    t = time.localtime()
    current_time = time.strftime("%D:%H:%M:%S", t)
    print(current_time)
    order_buy = client.create_order(symbol=symbol, side=Client.SIDE_BUY, type=Client.ORDER_TYPE_MARKET, quantity=quantity)
    print(order_buy)

# Schedule a job to run for the next 24 hours
schedule.every(1).hours.until(timedelta(hours=24)).do(job)

all_jobs = schedule.get_jobs()
print(all_jobs)

while True:
    schedule.run_pending()
    time.sleep(1)
