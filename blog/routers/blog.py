from typing import List
from fastapi import Depends, status, APIRouter
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blogDriver as blog


router = APIRouter(
    tags = ['blogs'],
    prefix = "/blog"
)

@router.get('/', response_model=List[schemas.ShowBlog], tags=['get'])
def all_blogs(db : Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED, tags=['post'])
def create(request : schemas.Blog, db : Session = Depends(get_db)):
    return blog.create(request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['delete'])
def destroy(id:int, db : Session = Depends(get_db)):
    return blog.destroy(id, db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED, tags=['put'])
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)


@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog, tags=['get'])
def show(id:int, db : Session = Depends(get_db)):
    return blog.getPost(id, db)