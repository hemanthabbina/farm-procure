from sqlalchemy import UUID, Column, Integer, String, ForeignKey
from app.database.connection import Base

class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"))
    bank_name = Column(String)
    branch = Column(String)
    account_number = Column(String)
    ifsc_code = Column(String)