from typing import List
import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.farmer import Farmer
from app.schemas.assignments import Assignment
from app.schemas.farmer import FarmerSchema
from sqlalchemy import any_, func

def get_farmer(db: Session, farmer_id: str):
    return db.query(Farmer).filter(Farmer.id == farmer_id).first()


def get_farmers_by_pincode(db: Session, assignments: list):
    result = db.query(Farmer.pincode, func.count(Farmer.id)).filter(Farmer.pincode == any_(assignments)).group_by(Farmer.pincode).all()
    for pincode, farmer_count in result:
        print(f"Pincode: {pincode}, Farmer Count: {farmer_count}")

    aggregated_results = [Assignment(pincode=pincode, farmer_count= farmer_count) for pincode, farmer_count in result]
    return aggregated_results

def create_farmer(db: Session, farmer: FarmerSchema):
    existing_farmer = get_farmer(db, farmer.id)
    if existing_farmer:
        existing_farmer.name = farmer.name
        existing_farmer.mobile = farmer.mobile
        existing_farmer.street = farmer.street
        existing_farmer.village = farmer.village
        existing_farmer.mandal = farmer.mandal
        existing_farmer.district = farmer.district
        existing_farmer.state = farmer.state
        existing_farmer.country = farmer.country
        existing_farmer.pincode = farmer.pincode
        db.add(existing_farmer)
        db.commit()
        db.refresh(existing_farmer)
        return existing_farmer
    else:
        print("Creat farmer")
        db_farmer = Farmer(name=farmer.name, mobile=farmer.mobile, street = farmer.street,
                            village = farmer.village, mandal = farmer.mandal, district = farmer.district,
                            state = farmer.state, country = farmer.country, pincode = farmer.pincode )
        print("Created farmer")
        db_farmer.id = str(uuid.uuid4())
        print(db_farmer.id)
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