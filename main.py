from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
#import uvicorn # ? Only needed for the commented section at the end

app = FastAPI()

"""
? Notes: 

? When setting up paths, you should put the exact matches above any dynamic blocks.

"""

@app.get('/blog') # get blogs-- get operation
# !Parameters:
## *limit - will default to 10 if not provided
## *published - will default to true if not specified 
## *sort - Optional field
### *Optional fields do not need to be added to the query at all and can be specified as None
def index(limit=10, published : bool=True, sort : Optional[str] = None):
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

class Blog(BaseModel):
    title : str
    body : str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog : Blog):
    return {'data': f"Blog is created with {blog.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000) # ? Allows for the change of address and port when running