from fastapi import FastAPI
from contextlib import asynccontextmanager
from data import create_tables, delete_tables
from router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("Database is reeady")
    yield
    print("Start")

app = FastAPI(lifespan=lifespan) 
app.include_router(router)