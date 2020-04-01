from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientForm


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
