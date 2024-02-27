from typing import Any

from pydantic import BaseModel, model_validator, SecretStr

from app.schemas.user import UserSchema


class RegisterCustomer(BaseModel):
    email: str
    password: SecretStr

    @model_validator(mode='after')
    def transform(self) -> UserSchema:
        return UserSchema(
            email=self.email,
            password=self.password.get_secret_value()
        )
