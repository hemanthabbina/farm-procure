from pydantic import BaseModel

class DealerSchema(BaseModel):
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

    assignments: list[str]

    class Config:
        orm_mode = True