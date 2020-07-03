# Don't Feel Blue, Jet Blue

Don't Feel Blue, Jet Blue is a web app that allows you and your airline to obtain real-time insights through sentiment analysis.
It was developed by Bhavesh Shah, Jonathan Wong, Jessica Ding, and Michael Liu at [YHack](https://yhack.org) 2019.

Slides are available [here](https://docs.google.com/presentation/d/1N0h9pwNU0eqOqePhaHeSEICEfx-Aw9I2nusYy7TcIRc/edit?usp=sharing).

## Install

You can clone this repo or download it as a zip.

```
git clone https://github.com/bhavrish/jetbluescrawler.git/
cd jetbluescrawler
```

Once you've done this, you should create a postgres database. You can do this from the shell.

```
createdb <DB_NAME>
```

You can assign relevant privileges. First enter psql.

```
psql <DB_NAME>
```

You can grant privileges from here.

```
GRANT ALL PRIVILEGES ON DATABASE <db_name> to <user>;
```

You'll now need to input your access credentials. You can do this by copying the .modelenv file in jetBlueWebApp and modifying it appropriately.
```
cp jetBlueWebApp/.modelenv jetBlueWebApp/.env
```

You can now install the packages and migrate the database to the models.

```
pipenv install
pipenv shell
python3 manage.py makemigrations
python3 manage.py migrate
```

If all of this works as expected, you should be able to now run the server.

```
python3 manage.py runserver
```

## Contributing

We don't currently have a guideline set in stone, but any popular OSS format works well, and we'll adopt one soon. Our project is super open to contributions.
