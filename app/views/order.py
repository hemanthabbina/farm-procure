from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.order import OrderSchema
from app.controllers import order as order_controller

router = APIRouter()

@router.post("/", response_model=OrderSchema)
def create_order_view(order: OrderSchema, db: Session = Depends(get_db)):
    return order_controller.create_order(db=db, order=order)

@router.get("/{order_id}", response_model=OrderSchema)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = order_controller.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/{order_id}", response_model=OrderSchema)
def update_order_view(order_id: int, order: OrderSchema, db: Session = Depends(get_db)):
    return order_controller.update_order(db=db, order_id=order_id, order=order)

@router.delete("/{order_id}")
def delete_order_view(order_id: int, db: Session = Depends(get_db)):
    return order_controller.delete_order(db=db, order_id=order_id)