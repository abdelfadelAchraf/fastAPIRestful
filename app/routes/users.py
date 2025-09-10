from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserCreate, UserResponse
from app.models.user import User
from app.db.dataBase import fake_users_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    new_user = User(id=len(fake_users_db) + 1, name=user.name, email=user.email)
    # check if the user with this email address exist or not 
    for u in fake_users_db:
        if u.email == user.email:
            return {"error": "User with this email already exists."}
    fake_users_db.append(new_user)
    return new_user

@router.get("/", response_model=list[UserResponse])
def get_users():
    return fake_users_db
