import uuid
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    email: str


class UserCreateRequest(BaseModel):
    name: str
    email: str
    password: str