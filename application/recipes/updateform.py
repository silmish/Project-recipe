from flask_wtf import FlaskForm
from wtforms import StringField, validators


class UpdateForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2)])
    new = StringField("Recipe new name", [validators.Length(min=2)])

    class Meta:
        csrf = False
