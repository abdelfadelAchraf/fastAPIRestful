from pydantic import BaseModel, EmailStr

# Request schema
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# Response schema
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
