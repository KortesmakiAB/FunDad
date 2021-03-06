"""Forms for FUN DAD app."""

from wtforms import StringField, PasswordField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from models import User


class UserSignupForm(FlaskForm):
    """New user signup form."""

    first_name     = StringField('first name', validators=[DataRequired()])
    last_name      = StringField('last name', validators=[DataRequired()])
    username_email = StringField('email address', validators=[DataRequired()])
    password       = PasswordField('password', validators=[Length(min=6)])


class UserLoginForm(FlaskForm):
    """Returning user login form."""

    username_email = StringField('email address', validators=[DataRequired()])
    password       = PasswordField('password', validators=[Length(min=6)])


class CheckInForm(FlaskForm):
    """CheckInForm"""

    destination = SelectField('destination', coerce=int, validators=[DataRequired()])


class NewDestinationForm(FlaskForm):
    """Add a new destination."""

    name    = StringField('destination name', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])


class EditDestinationForm(FlaskForm):
    """Edit a new destination."""

    name    = StringField('destination name', validators=[DataRequired()])

