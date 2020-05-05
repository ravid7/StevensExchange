# from yahoo_fin.stock_info import *
# from yahoo_fin.options import *
# from datetime import datetime

# current_date = datetime.today().strftime('%m/%d/%Y')
# data = get_data('gold', start_date='04/30/2020', end_date='05/02/2020')
# print(data.open, data.close)
from StevenEx import db
from StevenEx.models import User, Subscription
from StevenEx.identity import Identity

db.create_all()
passw = "gAAAAABesHz5C97H_QUTzHFQxRc9g1HEJNHoFEVjA33nNF_I7jCZcyBsU5iB7eI6LPsp0Xgdhuwv0SIfw0UKPoZe17PJh57nAQ=="
user = User(username="Ravi", email="ravid7.github", password=passw)
db.session.add(user)
db.session.commit()
user = User.query.get(1)
post = Subscription(item="This lil", user_id=user.id)
post1 = Subscription(item="This lil piece", user_id=user.id)
db.session.add(post)
db.session.add(post1)
db.session.commit()
i = Identity()
print(i.match(user.password, "7thatatters"))
db.drop_all()

