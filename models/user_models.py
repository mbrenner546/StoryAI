from datetime import date
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str = 'email@email'
    birthdate: str = '2022'
