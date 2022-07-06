from fastapi import FastAPI
import uvicorn

from app.core.config import settings
from app.api_v1.api import api_router
from app.db.session import Base, engine

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def start():
    """Launched with `poetry run start`"""
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
