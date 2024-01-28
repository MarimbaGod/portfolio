from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    status,
    HTTPException
)
import os
import bcrypt
from jwtdown_fastapi.authentication import Token
from queries.projects import ProjectRepository
from pydantic import BaseModel
from authenticator import authenticate_user
from typing import Union, List
import jwt
from datetime import datetime, timedelta


class AdminToken(Token):
    token: Token

router = APIRouter()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=20) # Expires in 20 mins
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.environ["SECRET_KEY"], algorithm="HS256")
    return encoded_jwt


@router.get("/admin/login")
async def admin_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if authenticate_user(form_data.username, form_data.password):
        #Generate JWT Token
        access_token = create_access_token(data={"sub": form_data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Incorrect Credentials")
