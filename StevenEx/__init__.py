 
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
#_init_
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

path = './StevenEx/databases'
access_right = 0o755
if not os.path.isdir(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
        exit()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ef7d72b3b1ec8f38952eb95b9bb6b6f1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/site.db'
db = SQLAlchemy(app)
db.create_all()
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from StevenEx import routes

# TODO: Delete list items