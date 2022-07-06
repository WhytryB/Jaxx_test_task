from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.session import Base


class Visitor(Base):
    id = Column(Integer, primary_key=True, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    visitors_count = Column(Integer)
    profile_name = Column(String(256), nullable=True)
