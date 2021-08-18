from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from pydantic.networks import HttpUrl
from .. import schemas, models
from ..database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(
    tags = ['user'],
    prefix = '/user'
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['post'])
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=['get'])
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"User with the id {id} is not available")
    return user