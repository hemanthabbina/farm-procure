from pydantic import BaseModel

class FarmSchema(BaseModel):
    id: int
    extent: int
    cocoa_plant_count: int
    year_planted: int

    class Config:
        orm_mode = True