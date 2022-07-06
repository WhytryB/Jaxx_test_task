from pydantic import BaseModel
from datetime import date


class VisitorBase(BaseModel):
    visitors_count: int
    profile_name: str
    time_created: date


class VisitorCreate(BaseModel):
    visitors_count: int
    profile_name: str

    class Config:
        orm_mode = True
