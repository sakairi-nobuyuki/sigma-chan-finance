# coding: utf-8

from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/")
async def smoke_test():
    print(f"smoking dayo (^ ^) at {datetime.datetime.now()}")

    return {"message": f"smoking dayo (^ ^) at {datetime.datetime.now()}"}


if __name__ == "__main__":
    print("smoke test dayo (^^)")