from sqlalchemy import Column, String, Integer, ForeignKey
from app.database.connection import Base

class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(String, primary_key=True, index=True)
    farmer_id = Column(String, ForeignKey("farmers.id"), index=True)
    type = Column(Integer)
    weight = Column(Integer)
    quality = Column(Integer)