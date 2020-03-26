from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=6, max=15)])
    password = PasswordField("Password", [validators.Length(min=6, max=20)])
    name = StringField("Name", [validators.Length(min=6, max=32)])

    class Meta:
        csrf = False