from pydantic import BaseModel

class Assignment(BaseModel):
    pincode: str

    class Config:
        orm_mode = True