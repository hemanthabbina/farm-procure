from typing import Optional
from pydantic import BaseModel, validator

from app.schemas.dealer import DealerSchema
from app.schemas.farmer import FarmerSchema

class OrderSchema(BaseModel):
    id: str
    date: str
    farmer: FarmerSchema
    dealer: Optional[DealerSchema] = None
    type: str
    quantity: int
    picture: str
    price: int
    status: str

    class Config:
        orm_mode = True



class CreateOrderSchema(BaseModel):
    id: str
    date: str
    farmer_id: str
    dealer_id: Optional[str] = None
    type: str
    quantity: int
    picture: str
    price: int
    status: str

    class Config:
        orm_mode = True

