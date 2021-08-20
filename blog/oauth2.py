from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

def get_current_user(JWTtoken: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate token",
        headers = {"WWW-Authenticate" : "Bearer"}
    )

    return token.verify_token(JWTtoken, credentials_exception)