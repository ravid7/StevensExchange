from datetime import datetime
from StevenEx import db


class User(db.Model):
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