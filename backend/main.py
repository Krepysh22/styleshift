from fastapi import FastAPI

from db import init_db
# import backend.db
from routers_main import router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


# DAL - DATA ACCESS LAYER

app.include_router(router)
app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

@app.on_event("startup")
async def on_startup():
    await init_db()


if __name__ == '__main__':
    print('qwe')