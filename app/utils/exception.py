from fastapi import Request
from fastapi.responses import JSONResponse

async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        content={"message": str(exc)}, 
        status_code=500)