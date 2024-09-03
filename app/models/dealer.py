from sqlalchemy import ARRAY, Column, Integer, String
from app.database.connection import Base

class Dealer(Base):
    __tablename__ = "dealers"

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

    assignments = Column(ARRAY(String))
