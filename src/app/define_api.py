from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .configuration import __version__, CORS_ORIGINS

from .routes import api_router

APP = FastAPI(
    title="REST API WITH EXAMPLES",
    summary="REST API WITH EXAMPLES",
    version=__version__
)

APP.include_router(
    router=api_router,
    tags=["Service 1: API endpoints"]
)

APP.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

