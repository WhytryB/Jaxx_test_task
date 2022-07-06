from fastapi import APIRouter
from app.api_v1.endpoints import visitors

api_router = APIRouter()
api_router.include_router(visitors.router, prefix="/visitor", tags=["visitor"])
