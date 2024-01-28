from pydantic import BaseModel
from typing import Optional
from queries.pool import pool

class ContactForm(BaseModel):
    name: str
    email: str
    message: str
