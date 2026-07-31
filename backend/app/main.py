from fastapi import FastAPI

from backend.app.core.config import settings
from backend.app.core.logger import logger

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION
)


@app.on_event("startup")
async def startup():
    logger.info("Application Started")


@app.get("/")
async def root():
    return {
        "project": settings.PROJECT_NAME,
        "status": "running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }