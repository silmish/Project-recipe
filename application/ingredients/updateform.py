from flask_wtf import FlaskForm
from wtforms import StringField, validators


class UpdateForm(FlaskForm):
    name = StringField("Ingredient name", [validators.Length(min=2)])
    new = StringField("Ingredient new name", [validators.Length(min=2)])

    class Meta:
        csrf = False
