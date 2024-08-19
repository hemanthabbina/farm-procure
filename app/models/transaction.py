from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from app.database.connection import Base

class Transaction(Base):
    __tablename__ = "transactions"

    date = Column(DateTime, primary_key=True)
    weight = Column(Integer)
    price = Column(Integer)
    total = Column(Integer)
    dealer_id = Column(String, ForeignKey("dealers.id"))
    farmer_id = Column(String, ForeignKey("farmers.id"))