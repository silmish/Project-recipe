from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from application import app, db
from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientForm
from application.ingredients.deleteform import IngredientDeleteForm
from application.ingredients.updateform import UpdateForm


@app.route("/ingredients", methods=["GET"])
@login_required
def ingredients_index():
    return render_template("ingredients/list.html", ingredients=Ingredient.query.all())


@app.route("/ingredients/new/")
@login_required
def ingredients_form():
    return render_template("ingredients/new.html", form=IngredientForm())


@app.route("/ingredients/new/", methods=["POST"])
@login_required
def ingredients_create():
    form = IngredientForm(request.form)

    if not form.validate():
        return render_template("ingredients/new.html", form=form)

    t = Ingredient(form.name.data)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("ingredients_index"))


@app.route("/ingredients/delete/", methods=["POST", "GET"])
@login_required
def ingredients_delete():
    form = IngredientDeleteForm(request.form)

    if not form.validate():
        return render_template("ingredients/delete.html", form=form)

    ingredient_delete = Ingredient.query.filter_by(name=form.name.data).first()

    if ingredient_delete is None:
        flash("Ingredient you are trying to delete do not exist", "warning")
    elif ingredient_delete.account_id != current_user.id:
        flash("You can only delete ingredients you have added yourself", "danger")
    else:
        flash("Ingredient has been deleted", "success")
        db.session().delete(ingredient_delete)
        db.session().commit()

    return redirect(url_for("ingredients_delete"))


@app.route("/ingredients/update/", methods=["POST", "GET"])
@login_required
def ingredients_update():
    form = UpdateForm(request.form)

    if not form.validate():
        return render_template("ingredients/update.html", form=form)

    update = Ingredient.query.filter_by(name=form.name.data).first()

    if update is None:
        flash("Ingredient you are trying to update do not exist", "warning")
    elif update.account_id != current_user.id:
        flash("You can only update ingredients you have added yourself", "danger")
    elif form.name.data.__len__() < 2 or form.new.data.__len__() < 2:
        flash("Ingredient name has to be longer than 1 character", "danger")
    else:
        flash("Ingredient name has been updated", "success")
        update.name = form.new.data
        db.session().commit()

    return redirect(url_for("ingredients_update"))



