import os
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    TIMESTAMP,
    BigInteger,
)

DB_URI = os.getenv("BOT_DB_URI")
engine = create_engine(DB_URI, echo=True)
meta = MetaData()

search_history = Table(
    "search_history",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", BigInteger, nullable=False),
    Column("search_term", String(255), nullable=False),
    Column("timestamp", TIMESTAMP, nullable=False),
)

meta.create_all(engine)
