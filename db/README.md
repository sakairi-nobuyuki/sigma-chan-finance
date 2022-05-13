# DB

## Migration by alembic

Initialize alembic ad `db` directory is already finished.

Migration by following command.

```
$ poetry run alembic revision --autogenerate -m "create table"
$ poetry run alembic upgrade head
```

You can find `time_series_inference.db` in the `db` directory.