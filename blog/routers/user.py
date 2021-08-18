from fastapi import Depends, status, APIRouter
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import userDriver as user

router = APIRouter(
    tags = ['user'],
    prefix = '/user'
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['post'])
def create_user(request: schemas.UserBase, db : Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=['get'])
def getSingle(id:int, db: Session = Depends(get_db)):
    return user.getSingle(id, db)
