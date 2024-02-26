from pydantic import BaseModel, SecretStr

from app.schemas.user import UserSchema


class RegisterCustomer(BaseModel):
    email: str
    password: SecretStr

    def transform(self) -> UserSchema:
        hash_password = self.password
        return UserSchema(
            email=self.email,
            password=hash_password
        )
