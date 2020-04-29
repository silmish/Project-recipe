from application import db

from application.recipe_ingredients.models import recipe_ingredients
from application.favorites.models import favorites


class Recipe(db.Model):
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(60), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    recipeIngredients = db.relationship('Ingredient', secondary=recipe_ingredients,
                                        backref=db.backref('recipe_ingredient', lazy='joined'))

    add_favorites = db.relationship('User', secondary=favorites,
                                    backref=db.backref('favorites', lazy='joined'))

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_recipes_with_ingredients():
        stmt = """SELECT recipe.id, recipe.name FROM recipe
                    LEFT JOIN recipe_ingredients ON recipe_ingredients.recipe_id = recipe.id
                    WHERE (ingredients_id IS NOT null)
                    GROUP BY recipe.id
                    HAVING COUNT(recipe_ingredients.ingredients_id) > 0"""
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response

    @staticmethod
    def get_recipe_count():
        stmt = """SELECT COUNT(DISTINCT recipe_id) FROM recipe_ingredients"""

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])

        return response

    @staticmethod
    def count_ingredient_recipe():
        stmt = """SELECT COUNT(recipe_ingredients.ingredients_id), recipe.name FROM recipe_ingredients
                            LEFT JOIN recipe ON recipe.id = recipe_ingredients.recipe_id
                            WHERE (recipe_id IS NOT null)
                            GROUP BY recipe.name
                            HAVING COUNT(recipe_ingredients.ingredients_id) > 0
                            ORDER BY COUNT(recipe_ingredients.ingredients_id) DESC
                            LIMIT 3"""
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            print(row[0])
            response.append({"id": row[0], "name": row[1]})

        return response

