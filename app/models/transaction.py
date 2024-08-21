from sqlalchemy import UUID, Column, String, Integer, DateTime, ForeignKey
from app.database.connection import Base

class Transaction(Base):
    __tablename__ = "transactions"

    date = Column(DateTime, primary_key=True)
    weight = Column(Integer)
    price = Column(Integer)
    total = Column(Integer)
    dealer_id = Column(Integer, ForeignKey("dealers.id"))
    farmer_id = Column(Integer, ForeignKey("farmers.id"))