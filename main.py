from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.config import settings
from app.controller.customer import customer_router
from app.controller.health import health_router
from app.dependency.exception import handle_custom_http_exception, handle_custom_validation_error
from app.helper.database import engine
from app.repositories.user import UserRepositories
from app.services.customer import CustomerServices


@asynccontextmanager
async def lifespan(app: FastAPI):
    user_repo = UserRepositories()

    customer_services = CustomerServices(user_repo=user_repo)

    yield {
        "customer_services": customer_services
    }
    await engine.dispose()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

# for add new custom exception handler
app.add_exception_handler(exc_class_or_status_code=HTTPException, handler=handle_custom_http_exception)
app.add_exception_handler(exc_class_or_status_code=RequestValidationError, handler=handle_custom_validation_error)

app.include_router(health_router)
app.include_router(customer_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
