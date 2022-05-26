# coding: utf-8

from pipeline import DatabaseOperation
#from db.pipeline import DatabaseOperation


import typer
import json

app = typer.Typer()


@app.command()
def insert_data(res: str):
    """Insert data to the DB. Sample command:
        $ poetry run python database.py "{\"type\": \"hoge\", \"name\": \"puiyo\", \"value\": 100.0, \"source\": \"fuga\"}"
    """
    print("Insert results to DB")
    res = json.loads(res)
    print("  res: ", res)
    db = DatabaseOperation()
    res = db.load_inference_results_model(res)
    db.insert(res)


if __name__ == "__main__":
    app()