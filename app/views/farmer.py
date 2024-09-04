from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.farmer import FarmerSchema
from app.controllers import farmer as farmer_controller

router = APIRouter()

@router.post("/", response_model=FarmerSchema)
def create_farmer_view(farmer: FarmerSchema, db: Session = Depends(get_db)):
    return farmer_controller.create_farmer(db=db, farmer=farmer)

@router.get("/{farmer_id}", response_model=FarmerSchema)
def read_farmer(farmer_id: str, db: Session = Depends(get_db)):
    db_farmer = farmer_controller.get_farmer(db, farmer_id=farmer_id)
    if db_farmer is None:
        raise HTTPException(status_code=404, detail="Farmer not found")
    return db_farmer

@router.put("/{farmer_id}", response_model=FarmerSchema)
def update_farmer_view(farmer_id: str, farmer: FarmerSchema, db: Session = Depends(get_db)):
    return farmer_controller.update_farmer(db=db, farmer_id=farmer_id, farmer=farmer)

@router.delete("/{farmer_id}")
def delete_farmer_view(farmer_id: str, db: Session = Depends(get_db)):
    return farmer_controller.delete_farmer(db=db, farmer_id=farmer_id)