from sqlalchemy import Column, String
from app.database.connection import Base

class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    mobile = Column(String)