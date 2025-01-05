from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..configuration import __version__

api_router = APIRouter()


@api_router.get("/health")
def health() -> JSONResponse:
    """
    Check if everything is working
    """
    status_code = 200
    return JSONResponse(
        content={'version': __version__},
        status_code=status_code
    )
