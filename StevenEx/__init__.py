 
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
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ef7d72b3b1ec8f38952eb95b9bb6b6f1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/site.db'
db = SQLAlchemy(app)


from StevenEx import routes