# coding: utf-8

import typer
import datetime

app = typer.Typer()


@app.command()
def smoke_test():
    print(f"smoking dayo (^ ^) at {datetime.datetime.now()}")


if __name__ == "__main__":
    app()    