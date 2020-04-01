from flask_wtf import FlaskForm
from wtforms import StringField, validators


class IngredientForm(FlaskForm):
    name = StringField("Ingredient name")

    class Meta:
        csrf = False