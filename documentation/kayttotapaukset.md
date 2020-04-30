# Käyttötapaukset

### Luo käyttäjatunnus tietokantaan (tehty)

Ensin tarkistetaan onko käyttäjä jo olemassa, eli onko username jo varattu.

Input on käyttäjän syöttämä tieto.

```
SELECT username FROM User
WHERE username ='Input';
```

Mikäi tämän vastaus on NONE tai NULL.

```
INSERT INTO User (name, username, password)
VALUES (Input name, Input username, Input password);
```

### Lisää resepti tietokantaan (tehty)

Input on käyttäjän syöttämä tieto.

```
SELECT name FROM Recipe
WHERE name ='Input';
```

Mikäi tämän vastaus on NONE tai NULL.

```
INSERT INTO Recipe (name)
VALUES (Input name);
```

Sama asia tehdään myös reseptiin kuuluvien ainesten osalta samaan aikaan kuin resepti lisätään.

SELECT name FROM Ingredient
WHERE name ='Input';

Mikäi tämän vastaus on None tai NULL.

```
INSERT INTO Ingredient (name)
VALUES (Input name);
```

Tämän jälkeen reseptin tiedot lisätään myös tauluun recipe_ingredients

```
INSERT INTO recipe_ingredients (recipe_id, ingredients_id)
VALUES (Input Recipe.id, Input Ingredient.id);
```

### Tarkastele reseptejä niiden omilla sivuillaan tarkemmin (tehty)

Linkki sivuilla luodaan reseptin id myötä, näin recipe_id tieto tulee linkistä.

```
SELECT id FROM Recipe
WHERE id ='recipe_id';
```

Reseptin tarkemmat tiedot haetaan yhdistelmätaulusta recipe_ingredients.

```
SELECT Recipe.id, Ingredient.id FROM Ingredient
LEFT JOIN recipe_ingredient ON recipe_ingredient.recipe_id = Recipe.id
LEFT JOIN Recipe on Recipe.id = recipe_ingredients.recipe_id
WHERE Recipe.id ='Input Recipe.id'
GROUP BY Recipe.id
HAVING COUNT(recipe_ingredients.ingredients_id) > 0;
```

Tästä tiedosta parsitaan reseptien nimi ja ainesten nimet jotka näytetään sivulla.

### Lisää reseptejä omaan profiiliin favorites listaukseen (tehty)

Kun on reseptin omalla sivulla on mahdollista lisätä resepti omaan favorites listaukseen painamalla nappia. Kun nappia painaa ensin haetaan reseptin tiedot ja sitten tarkistetaan onko resepti jo favorites listauksessa.

```
SELECT id FROM Recipe
WHERE id = 'Input id';
```

```
SELECT Recipe.id FROM Recipe
LEFT JOIN favorites ON favorites.recipe_id = 'Recipe.id'
WHERE favorites.recipe_id = 'Recipe.id';
```

Jos tämä on None tai NULL)

Lisätään tieto favorites tauluu tiedot jossa hyödynnetään tällähetkellä kirjautuneen käyttäjän tietoja, current_user:

```
INSERT INTO favorites (recipe_id, account_id)
VALUES (Recipe.id, current_user.id);
```

### Reseptejä jotka ovat favorites listalla voi myös tarkistella omasta profiilista tarkemmin (tehty)

Profiilille on vain luotu linkit reseptien omille sivuilla.

Profiiliin tuodaan favorites listalta reseptit näkyviin:

```
SELECT Recipe.id FROM Recipe
LEFT JOIN favorites ON favorites.recipe_id = Recipe.id
LEFT JOIN User on User.id = favorites.account_id
WHERE Recipe.id ='Input Recipe.id'
GROUP BY Recipe.id;
```

### Reseptejä ja raaka-aineita voi päivittää ja poistaa

Reseptien ja raaka-aineiden nimiä voi päivittää sovelluksessa. Käyttäjä syöttää nykyisen nimen ja uuden halutun nimen:

```
UPDATE Recipe
SET name = 'Input new name'
WHERE name = 'Input current name';

UPDATE Ingredient
SET name = 'Input new name'
WHERE name = 'Input current name';
```

Poisto tapahtuu:

```
DELETE FROM Recipe
WHERE name ='Input recipe name';

DELETE FROM Ingredient
WHERE name ='Input ingredient name';
```

Kummallakin toiminnolla on tarkiste että voi vain päivittää ja poistaa reseptejä ja raaka-aineita joita on itse luonut. Tässä hyödynnetään kirjautuneen käyttäjän tietoja.

```
SELECT account_id FROM Recipe
WHERE name ='Input recipe name';

SELECT account_id FROM Ingredient
WHERE account_id ='Input ingredient name';
```

Mikäli nämä eivät täsmää ei tietoja voi muuttaa.

### Sivuston statistiikkaa voi seurata statistics sivulta

Top 3 eniten käytettyä reseptiä:

```
SELECT COUNT(ingredients.id), ingredients.name FROM ingredients
LEFT JOIN recipe_ingredients ON recipe_ingredients.ingredients_id = ingredients.id
WHERE (recipe_id IS NOT null)
GROUP BY ingredients.name
HAVING COUNT(recipe_ingredients.ingredients_id) > 0
ORDER BY COUNT(ingredients.id) DESC
LIMIT 3;
```

Top 3 reseptiä missä eniten raaka-aineita:

```
SELECT COUNT(recipe_ingredients.ingredients_id), recipe.name FROM recipe_ingredients
LEFT JOIN recipe ON recipe.id = recipe_ingredients.recipe_id
WHERE (recipe_id IS NOT null)
GROUP BY recipe.name
HAVING COUNT(recipe_ingredients.ingredients_id) > 0
ORDER BY COUNT(recipe_ingredients.ingredients_id) DESC
LIMIT 3;
```


### Reseptejä voi hakea nimellä tai raaka-aineella (ei vielä tehty)

Kyseinen toiminto jäi tekemättä sairastelun takia, ei vain aika riittänyt.



