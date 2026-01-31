from fastapi import FastAPI
from app.api import router

app = FastAPI(title="People Counter API")
app.include_router(router)