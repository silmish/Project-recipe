from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField


class RecipeForm(FlaskForm):
    name = StringField("Recipe name")
    ingredientString = TextAreaField("Ingredients")

    class Meta:
        csrf = False
