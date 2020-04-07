from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.recipes.models import Recipe
from application.ingredients.models import Ingredient
from application.recipes.forms import RecipeForm


@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form=RecipeForm())


@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes=Recipe.query.all(),
                           has_ingredients=Recipe.find_recipes_with_ingredients())


@app.route("/recipes/new/", methods=["POST", "GET"])
@login_required
def recipes_create():
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/new.html", form=form)

    t = Recipe(form.name.data)
    t.account_id = current_user.id
    db.session().add(t)
    # db.session.flush()
    try:
        db.session().commit()
    except Exception as e:
        print(str(e))

    ingredients_string = form.ingredientString.data

    ingredients = [x.strip() for x in ingredients_string.split(',')]

    for ingredient in ingredients:
        x = db.session.query(Ingredient).filter(Ingredient.name == ingredient).one_or_none()

        if not x:
            x = Ingredient(ingredient)
            db.session().add(x)
            db.session().flush()
        try:
            db.session().commit()
        except Exception as e:
            print(str(e))

        t.recipeIngredients.append(x)
        db.session.flush()

    db.session.flush()
    try:
        db.session().commit()
    except Exception as e:
        print(str(e))

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
