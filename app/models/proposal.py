from sqlalchemy import UUID, Column, String, Integer, ForeignKey
from app.database.connection import Base

class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"), index=True)
    type = Column(Integer)
    weight = Column(Integer)
    quality = Column(Integer)