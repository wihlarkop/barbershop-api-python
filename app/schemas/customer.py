from pydantic import BaseModel, SecretStr, EmailStr

from app.helper.generator import generate_uuid
from app.entities.user import UserEntities


class RegisterCustomerRequest(BaseModel):
    email: EmailStr
    password: SecretStr

    def transform(self, hash_password: str) -> UserEntities:
        return UserEntities(
            uuid=generate_uuid(),
            email=self.email,
            password=hash_password
        )


class LoginCustomerRequest(BaseModel):
    email: EmailStr
    password: SecretStr


class LoginCustomerResponse(BaseModel):
    token: str
    refresh_token: str
