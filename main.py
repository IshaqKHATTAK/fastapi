from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get('/')
async def index():
    return {'response':'this is index route'}

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

@app.get('/about')
async def about():
    return  {'response':'this is about route'}

@app.get('abouot/id')
async def about_id(id):
    return {'response':id}

#query parameters
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/items/')
async def items(skip: int = 0, limit: int = 10):
    return {'response':fake_items_db[skip: skip+limit]}

#request body and post method

@app.post('/post')
async def data():
    return {'response':'data that is send'}

from pydantic import BaseModel, Field
class Intro(BaseModel):
    name: str = Field(examples=["namanam"])
    age: int | None = None
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )

@app.post('/into')
async def intro(info: Intro):
    return {'response':info}

items = {"foo": "The Foo Wrestlers"}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}