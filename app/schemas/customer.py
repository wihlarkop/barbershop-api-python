from pydantic import BaseModel, EmailStr

from app.entities.user import UserEntities
from app.helper.generator import generate_uuid


class RegisterCustomerRequest(BaseModel):
    email: EmailStr
    password: str

    def transform(self, hash_password: str) -> UserEntities:
        return UserEntities(
            uuid=generate_uuid(),
            email=str(self.email),
            password=hash_password
        )


class LoginCustomerRequest(BaseModel):
    email: EmailStr
    password: str


class LoginCustomerResponse(BaseModel):
    token: str
    refresh_token: str
