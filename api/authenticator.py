import os
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import bcrypt
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")


def authenticate_user(username: str, password: str):
    env_username = os.environ.get("USERNAME")
    env_password_hash = os.environ.get("HASHED_PASSWORD").encode()

    if bcrypt.checkpw(password.encode(), env_password_hash) and username == env_username:
        # User authenticated
        return True
    else:
        # Authentication Failed
        return False

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=20) # Expires in 20 mins
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.environ["SECRET_KEY"], algorithm="HS256")
    return encoded_jwt

async def validate_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, os.environ.get("SECRET_KEY"),  algorithms=["HS256"])
        return True
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication")
