from pydantic import BaseModel

class OrderSchema(BaseModel):
    id: int
    date: str
    farmer_id: int
    dealer_id: int
    type: str
    quantity: int
    picture: str
    price: int
    status: str

    class Config:
        orm_mode = True