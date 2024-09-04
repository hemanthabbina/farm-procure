from sqlalchemy import Column, String, Integer, ForeignKey
from app.database.connection import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True, index=True)
    date = Column(String)
    farmer_id = Column(String, ForeignKey("farmers.id"), index=True)
    dealer_id = Column(String, ForeignKey("dealers.id"), index=True, nullable=True)
    type = Column(String)
    quantity = Column(Integer)
    picture = Column(String)
    status = Column(String)
    price = Column(Integer)