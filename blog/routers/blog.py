from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from pydantic.networks import HttpUrl
from .. import schemas, models
from ..database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs','get'])
def all_blogs(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs','post'])
def create(request : schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1) #!temp hardcoding
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['blogs','delete'])
def destroy(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED, tags=['blogs','put'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update(request.dict())

    db.commit()
    return 'updated succesfully'


@router.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog, tags=['blogs','get'])
def show(id, response : Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")
        # // response.status_code = status.HTTP_404_NOT_FOUND
        # // return {'detail': f"Blog with the id {id} is not available"}

    return blog