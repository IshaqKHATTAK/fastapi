from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/')
async def index():
    return {'response':'this is index route'}

@app.get('/about')
async def about():
    return  {'response':'this is about route'}

@app.get('abouot/id')
async def about_id(id):
    return {'response':id}