from flask_wtf import FlaskForm
from wtforms import BooleanField


class FavoriteForm(FlaskForm):
    favorite = BooleanField("Add to favorites")

    class Meta:
        csrf = False