from sqlalchemy import Column, String, Integer, ForeignKey
from app.database.connection import Base
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True, index=True)
    date = Column(String)
    type = Column(String)
    quantity = Column(Integer)
    picture = Column(String)
    status = Column(String)
    price = Column(Integer)

    # Foreign keys and relationships
    farmer_id = Column(String, ForeignKey('farmers.id'))
    farmer = relationship('Farmer', backref='farmer_orders')
    dealer_id = Column(String, ForeignKey('dealers.id'), nullable=True)
    dealer = relationship('Dealer', backref='dealer_orders')