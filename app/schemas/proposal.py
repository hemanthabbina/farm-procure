from pydantic import BaseModel

class ProposalSchema(BaseModel):
    id: int
    farmer_id: int
    type: str
    weight: int
    quality: int

    class Config:
        orm_mode = True