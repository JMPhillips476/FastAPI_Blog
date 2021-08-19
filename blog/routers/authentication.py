from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash


router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login', tags=['post'])
def login(request:schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user or not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    return user