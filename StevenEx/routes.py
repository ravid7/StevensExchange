from StevenEx.models import User, Subscription
from yahoo_fin.stock_info import *
from yahoo_fin.options import *
from flask import Markup, render_template, url_for, flash, redirect, request
from StevenEx import app, db
from StevenEx.forms import RegisterationForm, LoginForm, SearchForm
from datetime import datetime
from StevenEx.identity import Identity
from flask_login import login_user, current_user, logout_user, login_required
from StevenEx.scrapper import *

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

time_crypto = datetime.utcnow()

crypto_labels = ['Symbol', 'Name', 'Price (Intraday)', 'Change', '% Change', 'Market Cap',
 'Volume in Currency (Since 0:00 UTC)', 'Volume in Currency (24Hr)',
 'Total Volume All Currencies (24Hr)', 'Circulating Supply']

crypto_content = []

initial_crypto = True

def live_price_editor():
    for i in range(len(top_labels)):
        final_label.append(top_labels[i] + " (%.2f)" % get_live_price(top_labels[i]))



@app.route('/home')
@app.route('/', methods=['GET', 'POST'])
def main():
    search_form = SearchForm(request.form)
    if request.method == 'POST':
        return redirect(url_for('search_results', result=search_form.search.data))
    return render_template('main_page.html', title="StevensEx Stock monitor", \
         top_labels=zip(color_strings, final_label, top_labels),
         form=search_form,  values=values, labels=labels, legend=legend)

# print(top_labels)

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


@app.route('/discovery/<result>')
def search_results(result):
    data = None
    if result:
        data = get_quote_table(result)
    return render_template("result.html", title=result, bulk=zip(data.keys(), data.values()))

@app.route('/cryptos')
def my_cryptos():
    global initial_crypto, crypto_content, crypto_labels, time_crypto
    mins = datetime.utcnow() - time_crypto
    if(initial_crypto or mins.seconds > 180):
        time_crypto = datetime.utcnow()
        initial_crypto = False
        table_name = 'crypto_data'
        top = get_top_crypto(22)
        top.to_sql(table_name, con=db.engine, if_exists='replace')
        crypto_content = db.engine.execute(f'SELECT * FROM {table_name}').fetchall()
    return render_template('cryptos.html', title="Crypto Currencies", 
    labels=crypto_labels, contents=(crypto_content))