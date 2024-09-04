from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.assignments import Assignment
from app.schemas.dealer import DealerSchema
from app.controllers import dealer as dealer_controller

router = APIRouter()

@router.post("/", response_model=DealerSchema)
def create_dealer_view(dealer: DealerSchema, db: Session = Depends(get_db)):
    return dealer_controller.create_dealer(db=db, dealer=dealer)

@router.get("/{dealer_id}", response_model=DealerSchema)
def read_dealer(dealer_id: str, db: Session = Depends(get_db)):
    db_dealer = dealer_controller.get_dealer(db, dealer_id=dealer_id)
    if db_dealer is None:
        raise HTTPException(status_code=404, detail="Dealer not found")
    return db_dealer

@router.get("/{dealer_id}/assignments", response_model=list)
def read_dealer(dealer_id: str, db: Session = Depends(get_db)):
    db_dealer = dealer_controller.get_dealer(db, dealer_id=dealer_id)
    if db_dealer is None:
        raise HTTPException(status_code=404, detail="Dealer not found")
    return db_dealer.assignments

@router.put("/{dealer_id}", response_model=DealerSchema)
def update_dealer_view(dealer_id: str, dealer: DealerSchema, db: Session = Depends(get_db)):
    return dealer_controller.update_dealer(db=db, dealer_id=dealer_id, dealer=dealer)

@router.delete("/{dealer_id}")
def delete_dealer_view(dealer_id: str, db: Session = Depends(get_db)):
    return dealer_controller.delete_dealer(db=db, dealer_id=dealer_id)
