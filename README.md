# 🪲 Bugza

Bugza is a bug tracking system. This is a REST API + GraphQL backend implementation of the system. A mobile and web app
implementation will follow up soon.

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
      poetry run python3 .\main.py
      ```

# Web Routes

All routes are available on `/docs` or `/redoc` paths with Swagger or ReDoc.   
To access **graphiql** or make **graphql** requests use the route `/graphql`

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
    + Project idea
    + [Use case diagram](https://www.freeprojectz.com/use-case/bug-tracking-system-use-case-diagram)
