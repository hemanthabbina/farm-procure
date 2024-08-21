from sqlalchemy import Column, String, Integer
from app.database.connection import Base

class Farm(Base):
    __tablename__ = "farms"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    extent = Column(Integer)
    cocoa_plant_count = Column(Integer)
    year_planted = Column(Integer)