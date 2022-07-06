from typing import Any
from fastapi import APIRouter, HTTPException

from app.crud.visitor import visitor
from app.schemas.visitor import VisitorCreate
from app.services.google_analytics import get_visitors
from app.db.session import SessionLocal

router = APIRouter()


@router.get("/get_visitors_count", status_code=200)
async def get_visitors_count(

) -> Any:
    """
    Retrieve visitors count.
    """
    profile_name, visitors_count = get_visitors()
    if not profile_name:
        raise HTTPException(
            status_code=404, detail=f"Visitors Not Found"
        )
    visitor_in = VisitorCreate(
        visitors_count=int(visitors_count),
        profile_name=profile_name,
    )
    async with SessionLocal() as session:
        async with session.begin():
            await visitor.create(session, obj_in=visitor_in)
    return visitors_count
