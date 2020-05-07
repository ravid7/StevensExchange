# from StevenEx import db
# from StevenEx.scrapper import *
# from datetime import datetime

# # current_date = datetime.today().strftime('%m/%d/%Y')
# data = get_top_crypto(5)
# data.to_sql('X', con=db.engine, if_exists='replace')
# v = db.engine.execute("SELECT * FROM X").fetchall()
# # print(data.columns.values)
# print(v[0])
# print(data.open, data.close)
from StevenEx import db
from time import sleep
from StevenEx.models import User, Subscription, Search, Currencies
from StevenEx.identity import Identity

# passw = "gAAAAABesHz5C97H_QUTzHFQxRc9g1HEJNHoFEVjA33nNF_I7jCZcyBsU5iB7eI6LPsp0Xgdhuwv0SIfw0UKPoZe17PJh57nAQ=="
# # user = User(username="Ravi", email="ravid7.github", password=passw)
# # user = User(username="xRavi", email="xravid7.github", password=passw)
# # db.session.add(user)
# # db.session.commit()
# # user = User.query.first()
# # # post = Subscription(item="This lil", user_id=user.id)
# # # post1 = Subscription(item="This lil piece", user_id=user.id)
# # # currency = Currencies(seperatedvalues="thisishsit")
# # # db.session.add(currency)
# # # db.session.add(post)
# # # db.session.add(post1)
# # search = Search(item="AAPL")
# # db.session.add(search)
# # db.session.commit()
# # x = (Search.query.filter(Search.item=='AAPL').limit(10).all())
# # for i in x:
# #     print(i)
# # i = Identity()
# # from datetime import datetime
# # curr = Currencies.query.first()
# # sleep(4)
# # date = datetime.utcnow() - curr.date
# # print(date.seconds > 3)
# db.drop_all()

from yahoo_fin.stock_info import *
from datetime import datetime, timedelta, date
# from models import Currencies
# v = get_day_gainers()
# print(v['Price (Intraday)'])
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
# print(get_day_gainers())
# data = (get_data("msft", interval = "1d", start_date = then_date , end_date = curr_date))
# x = (data['high'] + data['low'])/2
# print(x)
# import numpy as np
# ticker = "MSFT-C"
# # site = "https://finance.yahoo.com/quote/" + ticker + "?p=" + ticker

# tables = get_quote_table(ticker)
# print(tables    )
# # print(np.nan)
