"""SQLAlchemy models for FUN DAD."""

from datetime import date
from sqlalchemy.types import Date

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType

bcrypt = Bcrypt()
db = SQLAlchemy()


def connect_db(app):
    """Connect database to Flask app."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User account."""

    __tablename__ = 'users'

    id             = db.Column(db.Integer, primary_key=True)
    first_name     = db.Column(db.String(25), nullable=False)
    last_name      = db.Column(db.String(25), nullable=False)
    username_email = db.Column(db.String(25), nullable=False, unique=True)
    password       = db.Column(db.String(100), nullable=False)

    destinations   = db.relationship('Destination', secondary='users_destinations', backref='user')

    @classmethod
    def signup(cls, first_name, last_name, username_email, password):
        """Create user instance, inluding hashed pw, and add to session."""

        hashed_pw = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(first_name=first_name, last_name=last_name, username_email=username_email, password=hashed_pw)

        db.session.add(user)

        return user

    @classmethod
    def authenticate(cls, username_email, password):
        """Authenticate username/password combo."""

        user = cls.query.filter_by(username_email=username_email).first()

        if user:
            is_authenticated = bcrypt.check_password_hash(user.password, password)

            if is_authenticated:
                return user

        return False


class Destination(db.Model):
    """Places to take your kiddos."""

    __tablename__   = "destinations"

    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(100), nullable=False)
    place_id  = db.Column(db.String(200), nullable=False)
    latitude  = db.Column(db.Float, nullable=False)    
    longitude = db.Column(db.Float, nullable=False)

    visit_date = db.relationship('Visit', secondary='destinations_visits', backref='destination')


class UserDestination(db.Model):
    """User/Destination combination, a foreign key table."""

    __tablename__ = "users_destinations"

    id       = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.Integer, db.ForeignKey('users.id',  ondelete='cascade'), nullable=False)
    dest_id  = db.Column(db.Integer, db.ForeignKey('destinations.id',  ondelete='cascade'), nullable=False)


class DestinationVisit(db.Model):
    """visits and destinations join table."""

    __tablename__ = "destinations_visits"

    id       = db.Column(db.Integer, primary_key=True)
    dest_id  = db.Column(db.Integer, db.ForeignKey('destinations.id',  ondelete='cascade'), nullable=False)
    visit_id  = db.Column(db.Integer, db.ForeignKey('visits.id',  ondelete='cascade'), nullable=False)


class Visit(db.Model):
    """Date of a user's visit to a destination."""

    __tablename__ = "visits"

    id       = db.Column(db.Integer, primary_key=True)
    date     = db.Column(db.Date, nullable=False, default=date.today())
