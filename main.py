from fastapi import FastAPI

app = FastAPI()

"""
When setting up paths, you should put the exact matches above any dynamic blocks.

"""

@app.get('/blog') # get blogs-- get operation
def index(limit, published:bool):
    if published:
        return {'data':f'{limit} publsihed blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}


@app.get('/blog/{id}') #single blog show path -- get operation
def show(id:int):
    #fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id = id
    return {'data': {'1','2'}}