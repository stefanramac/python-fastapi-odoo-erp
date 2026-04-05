from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    name: str
    lastname: str
    phone: str
    email: EmailStr
    age: int
    nickname: str


class UserCreate(BaseModel):
    name: str
    lastname: str
    phone: str
    email: EmailStr
    age: int
    nickname: str