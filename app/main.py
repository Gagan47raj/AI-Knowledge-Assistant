from fastapi import FastAPI
from app.api.routes import router

from app.utils.exception import (
    generic_exception_handler
)



app = FastAPI(
    title="AI Knowledge Assistant"
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.include_router(router, prefix="/api/v1")