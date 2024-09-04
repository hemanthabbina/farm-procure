from typing import Optional
from pydantic import BaseModel, validator

class OrderSchema(BaseModel):
    id: int
    date: str
    farmer_id: int
    dealer_id: Optional[int] = None
    type: str
    quantity: int
    picture: str
    price: int
    status: str

    class Config:
        orm_mode = True