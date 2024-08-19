from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.farmer import Farmer
from app.schemas.farmer import FarmerSchema

def get_farmer(db: Session, farmer_id: str):
    return db.query(Farmer).filter(Farmer.id == farmer_id).first()

def create_farmer(db: Session, farmer: FarmerSchema):
    db_farmer = Farmer(id=farmer.id, name=farmer.name, address=farmer.address, mobile=farmer.mobile)
    db.add(db_farmer)
    db.commit()
    db.refresh(db_farmer)
    return db_farmer

def update_farmer(db: Session, farmer_id: str, farmer: FarmerSchema):
    db_farmer = get_farmer(db, farmer_id)
    if not db_farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    db_farmer.name = farmer.name
    db_farmer.address = farmer.address
    db_farmer.mobile = farmer.mobile
    db.commit()
    db.refresh(db_farmer)
    return db_farmer

def delete_farmer(db: Session, farmer_id: str):
    db_farmer = get_farmer(db, farmer_id)
    if not db_farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    db.delete(db_farmer)
    db.commit()