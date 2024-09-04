from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.order import OrderSchema
from app.controllers import order as order_controller
from fastapi_pagination import Page, add_pagination, paginate

router = APIRouter()

@router.post("/", response_model=OrderSchema)
def create_order_view(order: OrderSchema, db: Session = Depends(get_db)):
    return order_controller.create_order(db=db, order=order)



@router.get("/farmer/{farmer_id}", response_model=List[OrderSchema]) 
def list_all_orders(farmer_id: str, db: Session = Depends(get_db)):
    return order_controller.get_farmer_orders(db=db, farmer_id=farmer_id)


@router.get("/dealer/{dealer_id}", response_model=List[OrderSchema]) 
def list_all_orders(dealer_id: str, db: Session = Depends(get_db)):
    return order_controller.get_dealers_orders(db=db, dealer_id=dealer_id)

@router.get("/{order_id}", response_model=OrderSchema)
def read_order(order_id: str, db: Session = Depends(get_db)):
    db_order = order_controller.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/{order_id}", response_model=OrderSchema)
def update_order_view(order_id: str, order: OrderSchema, db: Session = Depends(get_db)):
    return order_controller.update_order(db=db, order_id=order_id, order=order)

@router.delete("/{order_id}")
def delete_order_view(order_id: str, db: Session = Depends(get_db)):
    return order_controller.delete_order(db=db, order_id=order_id)