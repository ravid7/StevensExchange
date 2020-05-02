'''
*****************************
**************
***************

***************
**************
*****************************
'''


from yahoo_fin.stock_info import *
from yahoo_fin.options import *
import pandas as pd
import sqlite3
from sqlite3 import Error
from flask import Flask, Markup, render_template

app = Flask(__name__)

top_labels = [
    "MSFT", "AAPL", "UBER", "GPRO",
    "LYFT", "TWTR", "NFLX", "TSLA"
]

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
        top_labels[i] += " (%.2f)" % get_live_price(top_labels[i])


@app.route('/')
def main():
    return render_template('main_page.html', title="StevensEx Stock monitor", labels=zip(color_strings, top_labels))

# print(top_labels)


if __name__ == '__main__':
    live_price_editor()
    app.run('127.0.0.1', 8080, debug=True)
