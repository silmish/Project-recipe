from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        flash("This username do not exist", "danger")
        return render_template("auth/loginform.html", form=form)

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html", form=LoginForm())


@app.route("/auth/new", methods=["POST"])
def auth_create():
    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form=form)

    u = db.session.query(User).filter(User.name == form.username.data).one_or_none()

    if u is not None:
        flash("This username already exists, please try a different one", "danger")
    elif form.username.data.__len__() < 6 or form.username.data.__len__() > 20:
        flash("Length of username has to be between 8 and 20 characters", "warning")
    elif form.password.data.__len__() < 8 or form.password.data.__len__() > 20:
        flash("Length of password has to be between 8 and 20 characters", "warning")
    elif form.name.data.__len__() < 6 or form.name.data.__len__() > 25:
        flash("Length of name has to be between 6 to 25 characters", "warning")
    else:
        flash("User has been created", "success")
        t = User(form.name.data, form.username.data, form.password.data)
        db.session().add(t)
        db.session().commit()

    return redirect(url_for("auth_create"))
