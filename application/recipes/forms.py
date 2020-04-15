from flask_wtf import FlaskForm
from wtforms import StringField, validators


class RecipeForm(FlaskForm):
    name = StringField("Recipe name")
    ingredientString = StringField("Ingredients")

    class Meta:
        csrf = False
