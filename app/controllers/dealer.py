import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.dealer import Dealer
from app.schemas.dealer import DealerSchema

def get_dealer(db: Session, dealer_id: str):
    return db.query(Dealer).filter(Dealer.id == dealer_id).first()

def create_dealer(db: Session, dealer: DealerSchema):
    db_dealer = Dealer(name=dealer.name, mobile=dealer.mobile, street = dealer.street,
                        village = dealer.village, mandal = dealer.mandal, district = dealer.district,
                        state = dealer.state, country = dealer.country, pincode = dealer.pincode , assignments = dealer.assignments)
    db_dealer.id = str(uuid.uuid4())
    print(db_dealer.id)
    db.add(db_dealer)
    db.commit()
    db.refresh(db_dealer)
    return db_dealer

def update_dealer(db: Session, dealer_id: str, dealer: DealerSchema):
    db_dealer = get_dealer(db, dealer_id)
    if not db_dealer:
        raise HTTPException(status_code=404, detail="Dealer not found")
    db_dealer.name = dealer.name
    db_dealer.mobile = dealer.mobile
    db_dealer.street = dealer.street
    db_dealer.village = dealer.village
    db_dealer.mandal = dealer.mandal
    db_dealer.district = dealer.district
    db_dealer.state = dealer.state
    db_dealer.country = dealer.country
    db_dealer.pincode = dealer.pincode
    db_dealer.assignments = dealer.assignments
    db.commit()
    db.refresh(db_dealer)
    return db_dealer
    

def delete_dealer(db: Session, dealer_id: str):
    db_dealer = get_dealer(db, dealer_id)
    if not db_dealer:
        raise HTTPException(status_code=404, detail="Dealer not found")
    db.delete(db_dealer)
    db.commit()