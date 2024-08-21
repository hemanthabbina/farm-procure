from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.dealer import Dealer
from app.schemas.dealer import DealerSchema

def get_dealer(db: Session, dealer_id: int):
    return db.query(Dealer).filter(Dealer.id == dealer_id).first()

def create_dealer(db: Session, dealer: DealerSchema):
    db_dealer = Dealer(name=dealer.name, address=dealer.address, mobile=dealer.mobile)
    db.add(db_dealer)
    db.commit()
    db.refresh(db_dealer)
    return db_dealer

def update_dealer(db: Session, dealer_id: int, dealer: DealerSchema):
    db_dealer = get_dealer(db, dealer_id)
    if not db_dealer:
        raise HTTPException(status_code=404, detail="Dealer not found")
    db_dealer.name = dealer.name
    db_dealer.address = dealer.address
    db_dealer.mobile = dealer.mobile
    db.commit()
    db.refresh(db_dealer)
    return db_dealer

def delete_dealer(db: Session, dealer_id: int):
    db_dealer = get_dealer(db, dealer_id)
    if not db_dealer:
        raise HTTPException(status_code=404, detail="Dealer not found")
    db.delete(db_dealer)
    db.commit()