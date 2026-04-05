from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.user_service import get_users, create_user, delete_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("")
def read_users():
    return get_users()

@router.post("")
def add_user(user: UserCreate):
    return create_user(user)

@router.delete("/{user_id}")
def remove_user(user_id: int):
    return delete_user(user_id)