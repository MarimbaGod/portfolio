import os
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwtdown_fastapi.authentication import Authenticator
import bcrypt
import jwt
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
# class MyAuthenticator(Authenticator):
#     async def get_account_data(
#         self,
#         username: str,
#         users: UserRepository,
#     ):
#         return users.get_user(username)

#     def get_account_getter(
#         self,
#         users: UserRepository = Depends(),
#     ):
#         return users

#     def get_hashed_password(self, user: UserOutWithPassword):
#         # Return encrypted password from userout with password object
#         return user.hashed_password

#     def get_account_data_for_cookie(self, user: UserIn):
#         # Return the username for the data for the cookie
#         # Return TWO values from this method
#         return user.username, UserOut(**user.dict())


# authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
