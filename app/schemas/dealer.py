from pydantic import BaseModel

class DealerSchema(BaseModel):
    id: str
    name: str
    address: str
    mobile: str

    class Config:
        orm_mode = True