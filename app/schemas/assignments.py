from pydantic import BaseModel


class Assignment(BaseModel):
    pincode: str
    farmer_count: int

    class Config:
        orm_mode = True
