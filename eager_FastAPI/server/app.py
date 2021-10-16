from fastapi import FastAPI
from typing import Optional, Text, Type
import asyncio
from server.routes.student import router
# from pymongo import MongoClient

# client = MongoClient


app = FastAPI()

app.include_router(router,tags=["Student"],prefix="/student")


@app.get("/",tags=["Root"], status_code=200)
async def read_root():
    return {"message":"here we go again ASYNC"}

@app.get("/a")
def root():
    return "hello Fast API"


@app.get("/stat")
def status():
    return {"status": "RUN RUN"}


@app.get("/wtf/{a}/{b}")
def sum(a, b=5):
    print(a, b)
    return {"sum": a + b}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    await asyncio.sleep(5)
    print(item_id)
    return {"item_id": item_id, "q": q}

