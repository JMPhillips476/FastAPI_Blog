from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from pydantic.networks import HttpUrl
from .. import schemas, models
from ..database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session


router = APIRouter(
    tags = ['blogs'],
    prefix = "/blog"
)

@router.get('/', response_model=List[schemas.ShowBlog], tags=['get'])
def all_blogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/', status_code=status.HTTP_201_CREATED, tags=['post'])
def create(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1) #!temp hardcoding
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['delete'])
def destroy(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED, tags=['put'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update(request.dict())

    db.commit()
    return 'updated succesfully'


@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog, tags=['get'])
def show(id, response : Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")

    return blog