from application import db

from application.recipe_ingredients.models import recipe_ingredients


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
                                        backref=db.backref('recipe_ingredient', lazy='dynamic'))

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

