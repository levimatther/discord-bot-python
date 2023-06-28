import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = os.getenv("BOT_DB_URI")
engine = create_engine(DB_URI, echo=True)

Session = sessionmaker(bind=engine)

session = Session()
