from application import db


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def count_ingredient_usage():
        stmt = """SELECT COUNT(ingredients.id), ingredients.name FROM ingredients
                        LEFT JOIN recipe_ingredients ON recipe_ingredients.ingredients_id = ingredients.id
                        WHERE (recipe_id IS NOT null)
                        GROUP BY ingredients.name
                        HAVING COUNT(recipe_ingredients.ingredients_id) > 0
                        ORDER BY COUNT(ingredients.id) DESC
                        LIMIT 3"""
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            print(row[0])
            response.append({"id": row[0], "name": row[1]})

        return response
