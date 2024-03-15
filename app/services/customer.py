from typing import NoReturn

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.helper.generator import hash_password, verify_password
from app.repositories.user import UserRepositories
from app.schemas.customer import LoginCustomer, RegisterCustomer


class CustomerServices:
    def __init__(self, user_repo: UserRepositories):
        self.__user_repo = user_repo

    async def register(self, payload: RegisterCustomer, session: AsyncSession) -> NoReturn:
        user = await self.__user_repo.get_user(email=payload.email, session=session)
        if user is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{user.email} already register")
        password = await hash_password(payload.password.get_secret_value())
        await self.__user_repo.create_user(payload=payload.transform(hash_password=password), session=session)
        return

    async def login(self, payload: LoginCustomer, session: AsyncSession) -> str:
        user = await self.__user_repo.get_user(email=payload.email, session=session)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{payload.email} not found")

        user = await verify_password(password=payload.password.get_secret_value(), hashed_password=user.password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="password is invalid")


        # generate jwt