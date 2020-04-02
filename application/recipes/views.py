from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.recipes.models import Recipe
from application.ingredients.models import Ingredient
from application.recipe_ingredients.models import recipe_ingredients
from application.recipes.forms import RecipeForm


@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form=RecipeForm())


@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes=Recipe.query.all())


@app.route("/recipes/new/", methods=["POST", "GET"])
@login_required
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    t = Recipe(form.name.data)
    ingredients_string = form.ingredientString.data
    print(ingredients_string)

    ingredients = ingredients_string.split(', ')

    print(ingredients)

    i = Ingredient.query.all()
    for name in i:
        print(name.name)

    """for ingredient in ingredients:
        x = Ingredient.query.one_or_none(name=ingredient)

        if not x:
            x = ingredient(ingredient)
            x.add()

        print(x)"""

    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("recipes_index"))


@app.route("/recipes/update/", methods=["POST", "GET"])
@login_required
def recipes_update():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/update.html", form=form)

    update = Recipe.query.filter_by(name=form.name.data).first_or_404()

    update.name = form.new.data

    db.session().commit()

    return redirect(url_for("recipes_index"))


@app.route("/recipe/delete/", methods=["POST", "GET"])
@login_required
def recipes_delete():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/delete.html", form=form)

    remove = Recipe.query.filter_by(name=form.name.data).first_or_404()

    db.session().delete(remove)
    db.session().commit()

    return redirect(url_for("recipes_index"))
