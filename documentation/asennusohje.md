# Asennusohje

Tarvittavat kirjastot ja paketit jotta sovelluksen voi saada paikallisesti käyttöön. Kun kaikki on asennettu voi sovelluksen ladata vaikka githubista ja lisätä kyseiseen kansioon.

## Sovelluksen asennus lokaalisti

Jotta sovelluksen voi saada lokaalisti toimimaan tulee ensin varmistaa että python3 on asennettu. Mikäli ei ole voi asennuksen tehdä Linuxilla esim:

```
sudo apt-get install python3
```

Tai osoitteesta: www.python.org/downloads/.

Seuraavaksi tarvitsee apukirjastojen lataukseen soveltuvan ohjelman, Python-pip.

Tämä onnistuu Linuxilla komenolla:

```
sudo apt install python3-pip
```

Jotta sovellusta pystyisi muokkaamaan ja käyttämään lokaalisti tulee Python virtuaaliympäristö, Python-venv, olla asennettuna. Tämä tuki luultavasti on asentunut Python3 asennuksen ohella.

Virtuaaliympäristön voi luoda haluttuun kansioon, esim:

```
mkdir demo
```
```
cd demo
```
```
python3 -m venv venv
```

Näin virtuaaliympäristö on luotu kansioon demo. Jotta virtuaaliympäristön vaa aktivoitua tulee kansion sisällä antaa seuraava komento:

```
source venv/bin/activate
```

Nyt virtuaaliympäristö on aktiivinen.

### Muita tarvittavia  kirjastoja

Kyseiset kirjastot tulee asentaa omaan virtaauliympärstöönsä, kuten esim demo kansioon.

Flask

```
pip install flask
```

sql-Alchemy

```
pip install flask-sqlalchemy
```

sqlite3

```
apt-get install sqlite3
```

Flask login

```
pip install flask-login
```

Flask WTF

```
pip install flask-wtf
```

## Sovelluksen asennus herokuun

Heroku käyttää Gunicorn-palvelinta käynnistäessään. Kyseisen kirjaston voi lisätä omaan sovellukseen komennolla:

```
pip install gunicorn
```

Jotta heroku osaisi käynnistyä oikein tarvitsee se tiedoston nimeltä Profcile, tiedoston voi luoda esimerkiski näin:

```
echo "web: gunicorn --preload --workers 1 application:app" > Procfile
```

Heroku käyttää palvelimillaan PostgreSQL tietokantana. Aikaisemmin on asennettu lokaalisti sqlite pelkästään. Postgre tuki asennetaan komennolla:

```
pip install psycopg2
```

Nyt meillä on valmuis saada heroku käyntiin ja tietokanta toimimaan.

Jotta saisimme sovelluksen tosin toimimaan herokussa tulee sille antaa vielä listaus eri riippuvuuksista jota se tarvitsee sovelluksen pyörittämiseen.

Riippuvuus lista luodaan tiedostoon requirements.txt näin:

```
pip freeze | grep -v pkg-recources > requirements.txt
```

Poistimme tiedon pkg-resource sillä se voi luoda ongelmia herokun kanssa.

Kun kaikki riippuvuudet on asennettu ja lisätty tiedostoon requirements.txt voi sen asentaa projektiin:

```
pip install -r requirements.txt
```

Nyt sovellus on valmis jotta sen vois lisätä herokuun. Varmista että sinulla on herokuun käyttäjätunnukset.

Luodaan seuraavaksi sovellukselle paikka herokuun:

```
heroku create sovelluksen-nimi
```

Nyt sinulla on oma heroku osoita ja github olemassa projektille.

Projektille pitää vielä lisätä tiedot herokun gitistä:

```
git remote add heroku 'heroku-git-osoite
```

Seuraavaksi lähetään herokuun:

```
git add .

git commit -m"Initial commit"

git push heroku master
```

Nyt projekti on herokussa ja sitä voi tarkistella omasta heroku osoitteesta jonka on luonut aikaisemmin.


Jotta herokuun saisi vielä tietokannan toiminaan tulee se luoda.

```
heroku addons:add heroku-postgresql:hobby-dev
```

Nyt herokussa on tietokanta myös käytössä, tiedot siirtyvät projektilta sinne kun ne pusketaan herokuun.
