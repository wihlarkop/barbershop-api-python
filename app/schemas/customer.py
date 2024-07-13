from pydantic import BaseModel, SecretStr, EmailStr

from app.helper.generator import generate_uuid
from app.schemas.user import UserSchema


class RegisterCustomer(BaseModel):
    email: EmailStr
    password: SecretStr

    def transform(self, hash_password: str) -> UserSchema:
        return UserSchema(
            uuid=generate_uuid(),
            email=self.email,
            password=hash_password
        )


class LoginCustomer(BaseModel):
    email: EmailStr
    password: SecretStr
