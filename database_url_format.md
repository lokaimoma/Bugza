# SQL Database URL formats for SQLAlchemy

## SQLITE

+ Synchronous
    + `sqlite:///database_path`
        + Example `sqlite:///./sql_app.db`
+ Asynchronous
    + Install `aiosqlite`
        + Poetry
          ```commandline
          poetry add aiosqlite
          ```
        + Pip
          ```commandline
          pip install aiosqlite
          ```
    + `sqlite+aiosqlite:///database_name.sqlite`

## MySQL & Maria DB

+ Install `aiomysql`, which will also install `pymysql`
    + Poetry
      ```commandline
      poetry add aiomysql
      ```
    + Pip
      ```commandline
      pip install aiomysql
      ```
    + Not all versions of `pymysql` work correctly with `aiomysql`, that's why we installed `aiomysql`
      before `pymysql`.
+ Synchronous
    + `mysql+pymysql://username:password@host:port/database_name`
+ Asynchronous
    + `mysql+aiomysql://username:password@host:port/database_name`

## PostgreSQL

+ Install `asyncpg`
    + Poetry
      ```commandline
      poetry add asyncpg
      ```
    + Pip
      ```commandline
      pip install asyncpg
      ```
+ Synchronous
    + `postgresql://username:password@host:port/database_name`
+ Asynchronous
    + `postgresql+asyncpg://username:password@host:port/database_name`

## Oracle

+ Install `cx-Oracle-async`
    + Poetry
      ````commandline
      poetry add cx-Oracle-async
      ````
    + Pip
      ```commandline
      pip install cx-Oracle-async
      ```
+ Synchronous
    + `oracle://username:password@host:port/sidname`
+ Asynchronous
    + `oracle+cx_Oracle_async://username:password@database_name`

## Others

Check out other database drivers from this [link](https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls)