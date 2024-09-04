from typing import Optional
from pydantic import BaseModel, validator

class OrderSchema(BaseModel):
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