from app.main import app
from app.models.visitor import Visitor
from app.core.config import settings

import pytest
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from httpx import AsyncClient


Base = orm.declarative_base()


@pytest.fixture(scope="session")
def engine():
    engine = create_async_engine(
        settings.SQLALCHEMY_DATABASE_URI
    )
    yield engine
    engine.sync_engine.dispose()


@pytest.fixture
async def session(engine):
    async with AsyncSession(engine) as session:
        yield session


@pytest.mark.asyncio
async def test_visitor(session):
    visitor_len = len((await session.execute(sa.select(Visitor))).scalars().all())
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("api_v1/visitor/get_visitors_count")
    assert response.status_code == 200
    assert len((await session.execute(sa.select(Visitor))).scalars().all()) == visitor_len + 1
