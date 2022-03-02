# 🪲 Bugza

A lite implementation of an issue tracking system. This is a REST API + GraphQL backend implementation of the system.

![Work FLow](https://github.com/lokaimoma/BUGZA/actions/workflows/run_tests.yml/badge.svg)

# Requirements

+ [Python 3.9+](https://www.python.org/downloads/)
+ [Poetry 1.1.12+](https://python-poetry.org/docs/#installation)

# Quickstart

+ Clone the project.

```commandline
git clone https://github.com/lokaimoma/Bugza
cd Bugza
```

+ Install app dependencies

```commandline
poetry install --no-root
```

+ Install an SQL database of your choice (if you haven't already) or you can choose to use SQLITE
+ Create a .env file in the project root (or rename .env.example to .env)
+ Add the following variables with their proper values.
    ```
    MODE = development / production (one of them)
    SYNC_DATABASE_URL = dialect+driver://username:password@host:port/database
    ASYNC_DATABASE_URL = dialect+driver://username:password@host:port/database
    SECRET_KEY = random generated secure key 
    ```
    + You can generate the **secrete key** with the command below. On Windows you will have to install OpenSSl first.
      For testing, just type any random number characters.
      ```commandline
      openssl rand -hex 32
      ```
    + For the **database url** format check this [file](database_url_format.md). MySQL and SQLite drivers are already
      installed by default, so you can skip installation for them in case you will be using one of them.
+ Create all database tables with the command
  ```commandline
  poetry run alembic upgrade head
  ```
+ Run the program with the command below.
    + Windows
      ```commandline
      poetry run python .\main.py
      ```
    + Linux & MacOS
      ```commandline
      poetry run python3 ./main.py
      ```

# Web Routes

App will be running on `localhost:8000` by default unless changed manually in the main.py file.   
All routes information are available on `/docs` or `/redoc` paths with Swagger or ReDoc.   
To access **graphiql** or make **graphql** requests use the route `/graphql`

# CORS

To enable CORS for your application :

+ Open `./app/__init__.py`
+ On line 12, add your URL to the origins list

```python
origins = [
    "http://localhost:3000",
]
```

+ And reload the app (Bugza)

# Run tests

All tests are defined in the `tests/` directory   
To run the tests, use the command

```commandline
poetry run pytest
```

# Technologies used

+ [FastAPI](https://fastapi.tiangolo.com/)
+ [SQLAlchemy](https://www.sqlalchemy.org/)
+ [Strawberry](https://strawberry.rocks/)
+ etc...

# Credits

+ [Free Projectz](https://www.freeprojectz.com/)
    + [Use case diagram](https://www.freeprojectz.com/use-case/bug-tracking-system-use-case-diagram)

# License

```
      
MIT License

Copyright (c) 2022 Owusu Kelvin Clark

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
