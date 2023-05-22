import os
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func

DATABASE_URL = 'postgresql+asyncpg://postgres:postgres@db:5432/styleshift_db'
    # os.environ.get("DATABASE_URL")
metadata_obj = MetaData()
Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# class Users(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     email_address = Column(String, nullable=False)

class Appeal(Base):
    __tablename__ = 'appeals'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    date_updated = Column(DateTime(timezone=True), onupdate=func.now())
    completed = Column(Boolean, default=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
