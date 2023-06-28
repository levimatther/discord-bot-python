from sqlalchemy import Column, Integer, String, TIMESTAMP, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SearchHistory(Base):
    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger)
    search_term = Column(String(255))
    timestamp = Column(TIMESTAMP)

    def __init__(self, user_id, search_term):
        self.user_id = user_id
        self.search_term = search_term
