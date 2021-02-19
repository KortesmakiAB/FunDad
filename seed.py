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

d4  = Destination(name="Bill Yeck Park",
                place_id="ChIJ8TgBwzWOQIgRdNKUGJjYdo4",
                latitude=39.625336,
                longitude=-84.118263)


db.session.add_all([d1, d2, d3, d4])
db.session.commit()


###############################################################
# User

u1 = User(first_name="Tom", last_name="Brady", username_email="tom@tb12.com", password="$2b$12$F9OhvGwLm9DDkuL8SqleTegr7GTkUm92S/0uAOy5mW7AcQbiUYhj.")
u2 = User(first_name="YoYo", last_name="Ma", username_email="yoyo@yoyoma.com", password="$2b$12$F9OhvGwLm9DDkuL8SqleTegr7GTkUm92S/0uAOy5mW7AcQbiUYhj.")

db.session.add_all([u1, u2])
db.session.commit()


###############################################################
# Visits

v1 = Visit()
v2 = Visit()
v3 = Visit()
v4 = Visit()

db.session.add_all([v1, v2, v3, v4])
db.session.commit()


###############################################################
# UserDestination

ud1 = UserDestination(user_id=2, dest_id=2)
ud2 = UserDestination(user_id=2, dest_id=3)
ud3 = UserDestination(user_id=2, dest_id=4)

db.session.add_all([ud1, ud2, ud3])
db.session.commit()

###############################################################
# DestinationVisit

dv1 = DestinationVisit(dest_id=2, visit_id=1)
dv2 = DestinationVisit(dest_id=3, visit_id=2)
dv3 = DestinationVisit(dest_id=3, visit_id=3)
dv4 = DestinationVisit(dest_id=4, visit_id=4)

db.session.add_all([dv1, dv2, dv3, dv4])
db.session.commit()