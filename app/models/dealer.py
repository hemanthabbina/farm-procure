from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Dealer(Base):
    __tablename__ = "dealers"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    mobile = Column(String)