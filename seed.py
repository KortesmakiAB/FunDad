from app import db
from models import *


db.drop_all()
db.create_all()

###############################################################
# Destinations

d1  = Destination(name="Southern Hills Playground",
                place_id="ChIJRdZFgIWGQIgRKRraAEvA2I0",
                latitude=39.72207068029149,
                longitude= -84.19479231970848)

d2  = Destination(name="Shafor Park",
                place_id="ChIJl1FxbDmEQIgRlW1utZH50Ng",
                latitude=39.7255265,
                longitude=-84.16824249999999)

d3  = Destination(name="Centennial Park at Houk Stream",
                place_id="ChIJJzjSCCyEQIgRQIeUXsPJqCQ",
                latitude=39.7165207,
                longitude=-84.18076789999999)


db.session.add_all([d1, d2, d3])
db.session.commit()


###############################################################
# User

u1  = User(first_name="Tom", last_name="Brady", username_email="tom@tb12.com", password="$2b$12$F9OhvGwLm9DDkuL8SqleTegr7GTkUm92S/0uAOy5mW7AcQbiUYhj.")

u2  = User(first_name="YoYo", last_name="Ma", username_email="yoyo@yoyoma.com", password="$2b$12$F9OhvGwLm9DDkuL8SqleTegr7GTkUm92S/0uAOy5mW7AcQbiUYhj.")

db.session.add_all([u1, u2])
db.session.commit()


###############################################################
# UserDestination

ud1 = UserDestination(user_id=2, dest_id=2)
ud2 = UserDestination(user_id=2, dest_id=3)

db.session.add_all([ud1, ud2])
db.session.commit()


###############################################################
# Visits

v1  = Visit(usr_dest=1)
v2  = Visit(usr_dest=2)

db.session.add_all([v1, v2])
db.session.commit()