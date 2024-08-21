from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.farmer import Farmer
from app.schemas.farmer import FarmerSchema

def get_farmer(db: Session, farmer_id: str):
    return db.query(Farmer).filter(Farmer.id == farmer_id).first()

def create_farmer(db: Session, farmer: FarmerSchema):
    db_farmer = Farmer(id=farmer.id, name=farmer.name, mobile=farmer.mobile, street = farmer.street,
                        village = farmer.village, mandal = farmer.mandal, district = farmer.district,
                        state = farmer.state, country = farmer.country, pincode = farmer.pincode )
    db.add(db_farmer)
    db.commit()
    db.refresh(db_farmer)
    return db_farmer

def update_farmer(db: Session, farmer_id: str, farmer: FarmerSchema):
    db_farmer = get_farmer(db, farmer_id)
    if not db_farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    db_farmer.name = farmer.name
    db_farmer.mobile = farmer.mobile
    db_farmer.street = farmer.street
    db_farmer.village = farmer.village
    db_farmer.mandal = farmer.mandal
    db_farmer.district = farmer.district
    db_farmer.state = farmer.state
    db_farmer.country = farmer.country
    db_farmer.pincode = farmer.pincode
    db.commit()
    db.refresh(db_farmer)
    return db_farmer

def delete_farmer(db: Session, farmer_id: str):
    db_farmer = get_farmer(db, farmer_id)
    if not db_farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    db.delete(db_farmer)
    db.commit()