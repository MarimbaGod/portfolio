from pydantic import BaseModel, EmailStr
from typing import Optional
from queries.pool import pool

class Contact(BaseModel):
    name: str
    phone: Optional[str] # Since phone numbers can be input by users in many ways
    email: EmailStr
    message: str

class ContactInDB(Contact):
    id: int
