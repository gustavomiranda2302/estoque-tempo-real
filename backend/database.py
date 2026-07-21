import os
from unittest.mock import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/partida_db")

ASYNC_DATABASE_URL = os.getenv(
    "ASYNC_DATABASE_URL", "postgresql+asyncpg://localhost/partida_db"
)

engine = create_engine(DATABASE_URL)
SessaoLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async_engine = create_async_engine(ASYNC_DATABASE_URL)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


def get_db():
    db = SessaoLocal()
    try:
        yield db
    finally:
        db.close()
