
from StevenEx import db
from time import sleep
from StevenEx.models import User, Subscription, Search, Currencies
from StevenEx.identity import Identity

from yahoo_fin.stock_info import *
from datetime import datetime, timedelta, date

def list_my_plot(ticker):
    curr = datetime.utcnow()
    diff = 20
    then = curr - timedelta(days=diff)
    curr_date = curr.strftime("%m/%d/%y")
    then_date = then.strftime("%m/%d/%y")
    chart_dates = []
    def perdelta(start, end, delta):
        curr = start
        while curr < end:
            yield curr
            curr += delta
    for  i in perdelta(date(then.year, then.month, then.day), 
    date(curr.year, curr.month, curr.day), timedelta(days=1)):
        chart_dates.append(i.strftime("%d/%m"))
    data = get_data(ticker, interval = "1d", start_date = then_date , end_date = curr_date)
    ave_value = (data['high'] + data['low'])/2
    return chart_dates, ave_value


print(list_my_plot('BTC-USD'))

