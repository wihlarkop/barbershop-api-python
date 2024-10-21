from typing import NoReturn

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncConnection

from app.exceptions.user_exception import UserAlreadyExists
from app.helper.generator import hash_password, verify_password
from app.repositories.user import UserInterface
from app.schemas.customer import LoginCustomerRequest, RegisterCustomerRequest


class CustomerServices:
    def __init__(self, user_repo: UserInterface):
        self.__user_repo = user_repo

    async def register(self, payload: RegisterCustomerRequest, conn: AsyncConnection) -> str:
        user = await self.__user_repo.get_user_by_email(email=payload.email, conn=conn)
        if user is not None:
            raise UserAlreadyExists(message=f"{user.email} already register")
        password = await hash_password(payload.password.get_secret_value())
        await self.__user_repo.create_user(payload=payload.transform(hash_password=password), conn=conn)
        return f"success register {payload.email}"

    async def login(self, payload: LoginCustomerRequest, conn: AsyncConnection) -> str:
        user = await self.__user_repo.get_user_by_email(email=payload.email, conn=conn)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{payload.email} not found")

        user = await verify_password(password=payload.password.get_secret_value(), hashed_password=user.password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="password is invalid")
        return ""
        # TODO generate jwt and return
