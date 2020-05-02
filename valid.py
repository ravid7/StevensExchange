from yahoo_fin.stock_info import *
from yahoo_fin.options import *
from datetime import datetime

current_date = datetime.today().strftime('%m/%d/%Y')
# print(get_calls('nflx', str(current_date)))
print(get_calls('nflx', "04/01/2020"))
