from my_app import db
from my_app.models import User
from random import randint


db.create_all()

for i in range(0,10):
    u = 'User' + str((randint(1,10000)))
    g = 'Guest' + str((randint(1,10000)))
    admin = User(username=u, email='admin@example.com')
    guest = User(username=g, email='guest@example.com')

    db.session.add(admin)
    db.session.add(guest)

    db.session.commit()


for user in  User.query.all():
    print (user) 

