# coding: utf-8

from db import DatabaseOperation

import typer

app = typer.Typer()


@app.command()
def insert_data():
    db = DatabaseOperation()
    


if __name__ == "__main__":
    app()