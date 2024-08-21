from pydantic import BaseModel

class BankAccountSchema(BaseModel):
    id: int
    farmer_id: int
    bank_name: str
    branch: str
    account_number: str
    ifsc_code: str

    class Config:
        orm_mode = True