# DB

## Migration by alembic

Initialize alembic ad `db` directory is already finished.

Migration by following command.

```
$ poetry run alembic revision --autogenerate -m "create table"
$ poetry run alembic upgrade head
```

You can find `time_series_inference.db` in the `db/volume` directory.

If you fail to migrate DB, run `$ poetry run alembic upgrade head` first, and after that run the migration program. 
Also `make revise_db` works similar to the migration program.

## Table design

See `models.py`.

## Insert DB

Insert data to the `inference_result` table.

```
$ poetry run python database.py "{\"type\": \"hoge\", \"name\": \"puiyo\", \"value\": 100.0, \"source\": \"fuga\"}"
```

## See data in the DB

```
$ cd volume
$ sqlite3 time_series_inference.db
> .schema
> select * from inference_result;
> .quit
```