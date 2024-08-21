from pydantic import BaseModel


class FarmerSchema(BaseModel):
    id: int
    name: str
    mobile: str

    street : str
    village : str
    mandal : str
    district : str
    state : str
    country : str
    pincode : str

    class Config:
        orm_mode = True