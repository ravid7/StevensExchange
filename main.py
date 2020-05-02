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

@app.route('/')
def main():
    return render_template('main_page.html', title="StevensEx Stock monitor")


if __name__ == '__main__':
    app.run('127.0.0.1', 5555, debug=True)
