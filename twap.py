from binance.client import Client
import json
from datetime import datetime, timedelta, time
import time
import schedule

#apì keys
api_key= ''
api_secret= ''
client = Client(api_key, api_secret)

# Symbol you wish to trade

symbol = 'BNBUSDT'
price = client.get_avg_price(symbol=symbol)

## TWAP BUY
# HOW MUCH OF THE ASSET YOU WISH TO BUY
quantity = 0.04
def job():
    t = time.localtime()
    current_time = time.strftime("%D:%H:%M:%S", t)
    print(current_time)
    order_buy = client.create_order(symbol=symbol, side=Client.SIDE_BUY, type=Client.ORDER_TYPE_MARKET, quantity=quantity)
    print(order_buy)

#run every minute
#schedule.every(1).minutes.do(job)

# Schedule a job to run for the next 24 hours
schedule.every(1).hours.until(timedelta(hours=24)).do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

## schedule examples
#schedule.every(10).seconds.do(job)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)


# run job until a 18:30 today
#schedule.every(1).hours.until("18:30").do(job)

# run job until a 2030-01-01 18:33 today
#schedule.every(1).hours.until("2030-01-01 18:33").do(job)

# Schedule a job to run for the next 8 hours
#schedule.every(1).hours.until(timedelta(hours=8)).do(job)

# Run my_job until today 11:33:42
#schedule.every(1).hours.until(time(11, 33, 42)).do(job)

# run job until a specific datetime
#schedule.every(1).hours.until(datetime(2020, 5, 17, 11, 36, 20)).do(job)
