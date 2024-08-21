from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    mobile = Column(String)

    street = Column(String)
    village = Column(String)
    mandal = Column(String)
    district = Column(String)
    state = Column(String)
    country = Column(String)
    pincode = Column(String)

