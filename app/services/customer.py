
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncConnection

from app.exceptions.user import UserAlreadyExists, UserNotFound
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
		password = await hash_password(payload.password)
		await self.__user_repo.create_user(
			payload=payload.transform(hash_password=password), conn=conn
		)
		return f"success register {payload.email}"

	async def login(self, payload: LoginCustomerRequest, conn: AsyncConnection) -> str:
		user = await self.__user_repo.get_user_by_email(email=payload.email, conn=conn)
		if user is None:
			raise UserNotFound(
				message=f"{payload.email} not found"
			)

		check_user_password = await verify_password(
			password=payload.password, hashed_password=user.password
		)
		if not check_user_password:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
		return ""
		# TODO generate jwt and return
