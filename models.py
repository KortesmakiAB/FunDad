"""SQLAlchemy models for FUN DAD."""

from datetime import datetime

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

    __tablename__   = 'users'

    id              = db.Column(db.Integer, primary_key=True)

    first_name      = db.Column(db.String(25), nullable=False)

    last_name       = db.Column(db.String(25), nullable=False)
    
    username_email  = db.Column(db.String(25), nullable=False, unique=True)

    password        = db.Column(db.String(100), nullable=False)

    
    @classmethod
    def signup(cls, first_name, last_name, username_email, password):
        """Create user instance, inluding hashed pw, and add to session."""

        hashed_pw   = bcrypt.generate_password_hash(password).decode('UTF-8')

        user        = User(first_name=first_name, last_name=last_name, username_email=username_email, password=hashed_pw)

        db.session.add(user)

        return user

    @classmethod
    def authenticate(cls, username_email, password):
        """Authenticate username/password combo."""

        user        = cls.query.filter_by(username_email=username_email).first()

        if user:
            is_authenticated = bcrypt.check_password_hash(user.password, password)

            if is_authenticated:
                return user

        return False


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

   