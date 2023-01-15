# coding: utf-8

import datetime
import typer


app = typer.Typer()


@app.command()
def smoke_test(job_id: str):
    print(f"smoking dayo (^ ^) at {datetime.datetime.now()} job_id: {job_id}")

    return {"message": f"smoking dayo (^ ^) at {datetime.datetime.now()}"}


@app.command()
def air_run(job_id: str):
    print(f"Air run shimasu (^o^) at {datetime.datetime.now()} job_id: {job_id}")

if __name__ == "__main__":
    app()