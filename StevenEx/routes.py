from StevenEx.models import User, Subscription, Search, Currencies
from yahoo_fin.stock_info import get_live_price, get_quote_table, get_data, _raw_get_daily_info
from yahoo_fin.options import *
from flask import Markup, render_template, url_for, flash, redirect, request
from StevenEx import app, db
from StevenEx.forms import RegisterationForm, LoginForm, SearchForm, AddLib
from datetime import datetime
from StevenEx.identity import Identity
from flask_login import login_user, current_user, logout_user, login_required
from StevenEx.scrapper import *
from datetime import datetime, timedelta, date
import random
# import numpy as np

legend = 'Monthly Data'
labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
values = [10, 9, 8, 7, 6, 4, 7, 8]

top_labels = [
    "MSFT", "AAPL", "UBER", "GPRO",
    "LYFT", "TWTR", "NFLX", "TSLA"
]

final_label = []

color_strings = [
    "list-group-item-primary",
    "list-group-item-secondary",
    "list-group-item-success",
    "list-group-item-danger",
    "list-group-item-warning",
    "list-group-item-info",
    "list-group-item-light",
    "list-group-item-dark"
]

time_crypto, time_stats = datetime.utcnow(), datetime.utcnow()

crypto_labels = ['Symbol', 'Name', 'Price (Intraday)', 'Change', '% Change', 'Market Cap',
 'Volume in Currency (Since 0:00 UTC)', 'Volume in Currency (24Hr)',
 'Total Volume All Currencies (24Hr)', 'Circulating Supply']

crypto_content, gainers, losers, actives = [], [], [], []

initial_crypto, initial_stats = True, True

def live_price_editor():
    for i in range(len(top_labels)):
        final_label.append(top_labels[i] + " (%.2f)" % get_live_price(top_labels[i]))

def ticker_info(ticker):
    site = "https://finance.yahoo.com/quote/" + ticker + "?p=" + ticker        
    tables = pd.read_html(site)
    try:
        return tables[0][1][0]
    except:
        return None

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

def get_day_most_active(max):
    
    return _raw_get_daily_info(f"https://finance.yahoo.com/most-active?offset=0&count={max}")
    # list_ = list(x.values.tolist())
    # return list_

def get_day_gainers(max):
    
    return  _raw_get_daily_info(f"https://finance.yahoo.com/gainers?offset=0&count={max}")
    # list_ = list(x.values.tolist())
    # return list_

def get_day_losers(max):
    
    return _raw_get_daily_info(f"https://finance.yahoo.com/losers?offset=0&count={max}")
    # list_ = list(x.values.tolist())
    # return list_

records = ['Symbol', 'Name', 'Price (Intraday)', 'Change', '% Change', 'Volume',
 'Avg Vol (3 month)', 'Market Cap', 'PE Ratio (TTM)']


# time_crypto = datetime.utcnow()
#         initial_crypto = False
#         table_name = 'crypto_data'
#         top = get_top_crypto(22)
#         top.to_sql(table_name, con=db.engine, if_exists='replace')
#         crypto_content = db.engine.execute(f'SELECT * FROM {table_name}').fetchall()

m_chart, m_val = [], []
chosen = 'MSFT'
@app.route('/home')
@app.route('/', methods=['GET', 'POST'])
def main():
    db.create_all()
    search_form = SearchForm(request.form)
    searched_items = Search.query.limit(10).all()
    if request.method == 'POST':
        search = Search(item=search_form.search.data)
        db.session.add(search)
        db.session.commit()
        return redirect(url_for('search_results', result=search_form.search.data))
    global initial_stats, gainers, losers, actives, time_stats, m_chart, m_val, chosen
    mins = datetime.utcnow() - time_stats
    if(initial_stats or (mins.seconds > 30*60)):
        initial_stats = False
        time_stats = datetime.utcnow()
        gainers_name, losers_name, actives_name = 'gainers_data', 'losers_data', 'actives_data'
        top_gainers, top_losers, top_actives = get_day_gainers(5), get_day_losers(5), get_day_most_active(5)
        top_gainers.to_sql(gainers_name, con=db.engine, if_exists='replace')
        top_losers.to_sql(losers_name, con=db.engine, if_exists='replace')
        top_actives.to_sql(actives_name, con=db.engine, if_exists='replace')
        gainers = db.engine.execute(f'SELECT * FROM {gainers_name}').fetchall()
        losers = db.engine.execute(f'SELECT * FROM {losers_name}').fetchall()
        actives = db.engine.execute(f'SELECT * FROM {actives_name}').fetchall()
        values = Currencies.query.all()
        if values:
            print("inside")
            size = len(values)
            item = random.randint(0,size-1)
            chosen = Currencies.query.get(item).seperatedvalues 
        else:
            chosen = 'MSFT'    
        m_chart, m_val = list_my_plot(chosen)
    return render_template('main_page.html', title="StevensEx Stock monitor", \
         top_labels=zip(color_strings, final_label, top_labels),
         form=search_form,  values=m_val, labels=m_chart, legend=legend, searched_items=searched_items, 
         records=records, gainers=gainers, losers=losers, actives=actives, chosen=chosen)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    register = RegisterationForm()
    if register.validate_on_submit():
        password = Identity().encrypt(register.password.data).decode()
        user = User(username=register.username.data, \
             email=register.email.data, password=password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {register.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Sign up", form=register)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
       return redirect(url_for('main'))
    login = LoginForm()
    if login.validate_on_submit():
        user = User.query.filter_by(email=login.email.data).first()
        if user and Identity().match(user.password, login.password.data):
            login_user(user, remember=login.remember.data)
            flash('You are logged in', 'success')
            return redirect(url_for('main'))
        else:
            flash('Make sure you enter your credentials correctly! Failed to login.', 'danger')
    return render_template('login.html', title="Sign in", form=login)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main'))


@app.route('/discovery/<result>', methods=['GET', 'POST'])
def search_results(result):  
    add = AddLib(request.form)
    check = Currencies.query.filter_by(seperatedvalues=result).scalar()
    if request.method == 'POST':
        if check:
            Currencies.query.filter_by(seperatedvalues=result).delete()
        else:
            curr = Currencies(seperatedvalues=result)
            db.session.add(curr)
            db.session.commit()
        return redirect(url_for('library'))
    if ticker_info(result) is None:
        flash('Invalid Entry', 'danger')
        return redirect(url_for('main'))
    data = get_quote_table(result)
    chart_dates, ave_value = list_my_plot(result)
    return render_template("result.html", title=result, bulk=zip(data.keys(), data.values()), \
    values=ave_value, labels=chart_dates, legend="20 dollars", button=current_user.is_authenticated, check=(check))

@app.route('/cryptos')
def my_cryptos():
    global initial_crypto, crypto_content, crypto_labels, time_crypto
    mins = datetime.utcnow() - time_crypto
    if(initial_crypto or mins.seconds > 5*60):
        time_crypto = datetime.utcnow()
        initial_crypto = False
        table_name = 'crypto_data'
        top = get_top_crypto(22)
        top.to_sql(table_name, con=db.engine, if_exists='replace')
        crypto_content = db.engine.execute(f'SELECT * FROM {table_name}').fetchall()
    return render_template('cryptos.html', title="Crypto Currencies", 
    labels=crypto_labels, contents=(crypto_content))


@app.route('/lib')
def library():
    if not current_user.is_authenticated:
        return redirect(url_for('main'))
    currency = Currencies.query.all()
    return render_template('library.html', data=currency)