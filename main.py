from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {'response':'this is index route'}

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

from pydantic import BaseModel
class Intro(BaseModel):
    name: str
    age: int | None = None
    description: str | None = None

@app.post('/into')
async def intro(info: Intro):
    return {'response':info}