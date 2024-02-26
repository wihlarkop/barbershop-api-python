from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user import UserRepositories
from app.schemas.customer import RegisterCustomer


class CustomerServices:
    def __init__(self, user_repo: UserRepositories):
        self.__user_repo = user_repo

    async def register(self, payload: RegisterCustomer, session: AsyncSession):
        user = await self.__user_repo.get_user(email=payload.email, session=session)
        print(user)

    async def login(self):
        pass
