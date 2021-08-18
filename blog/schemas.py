from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title : str
    body : str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class User(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True

class ShowUser(User):
    blogs: List[Blog] = []
    
class ShowBlog(Blog):
    creator: User
    