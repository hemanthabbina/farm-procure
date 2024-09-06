from pydantic import BaseModel

from app.schemas.dealer import DealerSchema
from app.schemas.farmer import FarmerSchema

class SummarySchema(BaseModel):
    pincode: str
    registeredFarmers: int
    pendingOrdersCount: int
    pendingOrdersSize: int
    acceptedOrdersCount: int
    acceptedOrdersSize: int
    rejectedOrdersCount: int
    rejectedOrdersSize: int
    completedOrdersCount: int
    completedOrdersSize : int

    class Config:
        orm_mode = True