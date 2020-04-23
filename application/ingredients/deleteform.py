from flask_wtf import FlaskForm
from wtforms import StringField, validators


class IngredientDeleteForm(FlaskForm):
    name = StringField("Ingredient name", [validators.Length(min=2)])

    class Meta:
        csrf = False