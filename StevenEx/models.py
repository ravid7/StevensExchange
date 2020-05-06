from datetime import datetime
from StevenEx import db, login_manager
from flask_login import UserMixin

# login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    subs = db.relationship('Subscription', backref='editor', lazy=True)

    def __repr__(self):
        return f'User(\'{self.username}\', \'{self.email}\')'
    
class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f'User(\'{self.item}\', \'{self.date}\')'

class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f'User(\'{self.item}\')'    


# class Currencies(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     seperatedvalues = db.Column(db.String(2000), nullable=True)
#     date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __repr__(self):
#         return f'Currencies(\'{self.seperatedvalues}\',\'{self.date}\')'