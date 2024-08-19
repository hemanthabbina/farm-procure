from pydantic import BaseModel

class ProposalSchema(BaseModel):
    id: str
    farmer_id: str
    type: str
    weight: int
    quality: int

    class Config:
        orm_mode = True