from flask_wtf import FlaskForm
from wtforms import StringField, validators


class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2)])
    new = StringField("Recipe new name")
    ingredientString = StringField("Ingredients")

    class Meta:
        csrf = False
