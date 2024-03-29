from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    status,
    HTTPException
)
import os
from queries.projects import Project, ProjectInDB, ProjectRepository


# from jwtdown_fastapi.authentication import Token
from fastapi.security import OAuth2PasswordRequestForm
from queries.projects import ProjectRepository
from pydantic import BaseModel
from authenticator import authenticate_user, validate_token
from typing import Union, List
import jwt
from datetime import datetime, timedelta


# class AdminToken(Token):
#     token: Token

router = APIRouter()
project_repo = ProjectRepository()

class HttpError(BaseModel):
    detail: str


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=20) # Expires in 20 mins
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.environ["SECRET_KEY"], algorithm="HS256")
    return encoded_jwt


@router.post("/admin/login")
async def admin_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if authenticate_user(form_data.username, form_data.password):
        #Generate JWT Token
        access_token = create_access_token(data={"sub": form_data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Incorrect Credentials")


@router.post("/admin/projects/add", response_model=ProjectInDB)
async def add_project(project: Project, _ = Depends(validate_token)):
    new_project = project_repo.add_project(project)
    return new_project


@router.delete("/admin/projects/delete", response_model=bool | HttpError)
async def delete_project(project: Project, _ = Depends(validate_token)):
