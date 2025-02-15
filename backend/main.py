from typing import Union

from fastapi import FastAPI

app = FastAPI()

"""
Template code for now this will be the main entry point for FAST API

Include routers for API endpoints
"""


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

