# Tietokanta

Tietokanta sisältää päätaulut Recipe, User ja Ingredient.

Recipe ja Ingredient taulun välissä on liitostaulu, recipe_ingredient.

User ja Recipe taululilla liitostaulu favorites.

Tietokanta on normalisoitu.


![Tietokantakaavio](https://github.com/silmish/Project-recipe/blob/master/documentation/Tietokantakaavio.jpg)

```
Recipe (int id, date_created datetime, date_modified datetime, name string, account_id FK (account.id)

CREATE TABLE Recipe (```
id int PRIMARY KEY,
date_created DateTime,
date_modified DateTime,
name string,
account_id int FOREIGN KEY REFERENCE User('id')
);
```

```
User (int id, date_created datetime, date_modified datetime, name string, usernmane string, password string)

CREATE TABLE User (
id int PRIMARY KEY,
date_created DateTime,
date_modified DateTime,
name string,
username string,
password string
);
```

```
Ingredient(id int, name string, account_id int FK (account.id)

CREATE TABLE Ingredient (
id int PRIMARY KEY,
name string,
account_id int FOREIGN KEY REFERENCE User('id')
);
```

```
recipe_ingredients (recipe_id FK (Recipe.id), ingredients_id (Ingredient.id))

CREATE TABLE recipe_ingredients (
recipe_id int FOREIGN KEY REFERENCE Recipe('id'),
ingredients_id FOREIGN KEY REFERENCE Ingredient('id')
);
```

```
favorites (recipe_id FK (Recipe.id), account_id FK (User.id))

CREATE TABLE favorites (
recipe_id FOREIGN KEY REFERENCE Recipe('id'),
account_id FOREIGN KEY REFERENCE User('id')
); 
```


