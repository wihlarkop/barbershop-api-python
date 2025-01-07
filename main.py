import os
import signal
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import ORJSONResponse

from app.config import settings
from app.controller.customer import customer_router
from app.controller.health import health_router
from app.controller.product import product_router
from app.controller.store import store_router
from app.controller.transaction import transaction_router
from app.database.client import engine
from app.exceptions.base import InternalServerError, create_exception_handler, exception_handlers
from app.repositories.product import ProductRepositories
from app.repositories.store import StoreRepositories
from app.repositories.user import UserRepositories
from app.services.customer import CustomerServices
from app.services.product import ProductServices
from app.services.store import StoreServices


@asynccontextmanager
async def lifespan(app: FastAPI):
    user_repo = UserRepositories()
    product_repo = ProductRepositories()
    store_repo = StoreRepositories()

    customer_services = CustomerServices(user_repo=user_repo)
    product_services = ProductServices(product_repo=product_repo)
    store_services = StoreServices(store_repo=store_repo)

    yield {
        "customer_services": customer_services,
        "product_services": product_services,
        "store_services": store_services,
    }
    await engine.dispose()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
    exception_handlers=exception_handlers,
)

app.include_router(health_router)
app.include_router(customer_router)
app.include_router(product_router)
app.include_router(store_router)
app.include_router(transaction_router)

if __name__ == "__main__":
    try:
        uvicorn.run(
            app="main:app",
            host=settings.HOST,
            port=settings.PORT,
            reload=settings.DEBUG,
        )
    except KeyboardInterrupt:
        pass
    finally:
        os.kill(os.getpid(), signal.SIGINT)
