'''
**************************************

<<<<<<<<<<<<<<<<<<<<<<<<<<|>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<   >>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<                  >>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<      -------------      >>>>>>>>>>>>>>
<<<<<<< rrathor2@stevens.edu, ravid7.github.io >>>>>>>
<<<<<<<<<<<<<<                          >>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<                  >>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<   >>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<|>>>>>>>>>>>>>>>>>>>>>>>>>>>

**************************************
'''

from yahoo_fin.stock_info import *
from yahoo_fin.options import *
import pandas as pd
import sqlite3
from sqlite3 import Error
from flask import Flask, Markup, render_template, url_for, flash, \
    redirect
from signin_login import RegisterationForm, LoginForm

app = Flask(__name__)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]


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


def live_price_editor():
    for i in range(len(top_labels)):
        final_label.append(top_labels[i] + " (%.2f)" % get_live_price(top_labels[i]))


@app.route('/')
def main():
    line_labels = labels
    line_values = values
    return render_template('main_page.html', title="StevensEx Stock monitor", \
         top_labels=zip(color_strings, final_label), max=17000, labels=line_labels, values=line_values)

# print(top_labels)

@app.route("/register", methods=['GET', 'POST'])
def register():
    register = RegisterationForm()
    if register.validate_on_submit():
        flash(f'Account created for {register.username.data}!', 'success')
        return redirect(url_for('main'))
    return render_template('register.html', title="Sign up", form=register)

@app.route("/login", methods=['GET', 'POST'])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        # flash(f'')
        if login.email.data == 'xxx@gmail.com':
            flash('You are logged in', 'success')
            return redirect(url_for('main'))
        else:
            flash('Make sure you enter your credentials correctly! Failed to login.', 'danger')
    return render_template('login.html', title="Sign in", form=login)

if __name__ == '__main__':
    live_price_editor()
    app.config['SECRET_KEY'] = 'ef7d72b3b1ec8f38952eb95b9bb6b6f1'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://site.db'
    app.run('127.0.0.1', 8080, debug=True)
