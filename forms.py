"""Forms for FUN DAD app."""

# from wtforms import SelectField
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from models import User

BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class UserSignupForm(ModelForm):
    """Form for adding new users."""

    class Meta:
        model = User






# class NewSongForPlaylistForm(FlaskForm):
#     """Form for adding a song to playlist."""

#     song = SelectField('Song To Add', coerce=int)
