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

