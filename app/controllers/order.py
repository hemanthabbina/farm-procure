from sqlalchemy import any_
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.dealer import Dealer
from app.models.farmer import Farmer
from app.models.order import Order
from app.schemas.order import OrderSchema

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def get_orders(db: Session):
    return db.query(Order).all()

def get_farmer_orders(db: Session, farmer_id: int):
    return db.query(Order).filter(Order.farmer_id == farmer_id)

def get_dealers_orders(db: Session, dealer_id: int):
    print("get_dealers_orders")
  #   assignments = db.query(Dealer).filter(Dealer.id == dealer_id).
  #  assignment_list = list(Dealer.assignments).options(load_only("id")).\
  #  print(assignment_list)
 #   return db.query(Farmer, Order, Dealer).filter(Order.farmer_id == Farmer.id).filter(Farmer.pincode == assignment_list.index[0])
    return db.query(Order).join(Farmer).join(Dealer).filter(Dealer.id == dealer_id).filter(Order.farmer_id == Farmer.id).filter(Farmer.pincode == any_(Dealer.assignments))


def create_order(db: Session, order: OrderSchema):
    db_order = Order(farmer_id=order.farmer_id, dealer_id= order.dealer_id, date=order.date, type=order.type, quantity=order.quantity, picture=order.picture, price=order.price, status=order.status)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order(db: Session, order_id: int, order: OrderSchema):
    db_order = get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.farmer_id = order.farmer_id
    db_order.dealer_id = order.dealer_id
    db_order.type = order.type
    db_order.quantity = order.quantity
    db_order.picture = order.picture
    db_order.price = order.price
    db_order.status = order.status
    db_order.date = order.date
    db.commit()
    db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()