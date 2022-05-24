# coding: utf-8

from pipeline import DatabaseOperation
#from db.pipeline import DatabaseOperation


import typer
import json

app = typer.Typer()


@app.command()
def insert_data(res: str):
    print(res)
    res = json.loads(res)
    db = DatabaseOperation()
    res = db.load_inference_results_model(res)
    db.insert(res)


if __name__ == "__main__":
    app()