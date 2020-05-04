# from yahoo_fin.stock_info import *
# from yahoo_fin.options import *
# from datetime import datetime

# current_date = datetime.today().strftime('%m/%d/%Y')
# data = get_data('gold', start_date='04/30/2020', end_date='05/02/2020')
# print(data.open, data.close)
from main import db, User, Subscription


db.create_all()
user = User(username="Ravi", email="ravid7.github", password="sdfsdfs")
user1 = User(username="dsRavi", email="ravidsd7.github", password="dssdfsdfs")
db.session.add(user)
db.session.add(user1)
db.session.commit()
user = User.query.get(1)
post = Subscription(item="This lil", user_id=user.id)
post1 = Subscription(item="This lil piece", user_id=user.id)
db.session.add(post)
db.session.add(post1)
db.session.commit()
print(user.subs)
db.drop_all()

