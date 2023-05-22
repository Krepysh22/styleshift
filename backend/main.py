from fastapi import FastAPI

from db import init_db
# import backend.db
from routers_main import router

app = FastAPI()


# DAL - DATA ACCESS LAYER

app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await init_db()


if __name__ == '__main__':
    print('qwe')