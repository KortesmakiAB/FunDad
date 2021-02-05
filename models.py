"""SQLAlchemy models for FUN DAD."""

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


def connect_db(app):
    """Connect database to Flask app."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User account."""

    __tablename__   = 'users'

    id              = db.Column(db.Integer, primary_key=True)

    username        = db.Column(db.String(25), nullable=False, unique=True)

    password        = db.Column(db.String(100), nullable=False)

    email           = db.Column(db.String(50), nullable=False, unique=True)


class Destination(db.Model):
    """Places to take your kiddos."""

    __tablename__   = "destinations"

    id              = db.Column(db.Integer, primary_key=True)

    place_id        = db.Column(db.String(200), nullable=False, unique=True)

    latitude        = db.Column(db.Float, nullable=False)
    
    longitude       = db.Column(db.Float, nullable=False)


class User_Destination(db.Model):
    """User/Destination combination, goreign key table"""

    __tablename__   = "users_destinations"

    user_id         = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'), primary_key=True)
    
    dest_id         = db.Column(db.Integer, db.ForeignKey('destinations.id', ondelete='cascade'), primary_key=True)

   