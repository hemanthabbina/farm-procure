from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.bankaccount import BankAccount
from app.schemas.bankaccount import BankAccountSchema

def get_bankaccount(db: Session, bankaccount_id: str):
    return db.query(BankAccount).filter(BankAccount.id == bankaccount_id).first()

def create_bankaccount(db: Session, bankaccount: BankAccountSchema):
    db_bankaccount = BankAccount(id=bankaccount.id, farmer_id=bankaccount.farmer_id, bank_name=bankaccount.bank_name, branch=bankaccount.branch, account_number= bankaccount.account_number,ifsc_code=bankaccount.ifsc_code)
    db.add(db_bankaccount)
    db.commit()
    db.refresh(db_bankaccount)
    return db_bankaccount

def update_bankaccount(db: Session, id: str, bankaccount: BankAccountSchema):
    db_bankaccount = get_bankaccount(db, id)
    if not db_bankaccount:
        raise HTTPException(status_code=404, detail="Bank Account not found")
    db_bankaccount.name = bankaccount.name
    db_bankaccount.address = bankaccount.address
    db_bankaccount.mobile = bankaccount.mobile
    db.commit()
    db.refresh(db_bankaccount)
    return db_bankaccount

def delete_bankaccount(db: Session, id: str):
    db_bankaccount = get_bankaccount(db, id)
    if not db_bankaccount:
        raise HTTPException(status_code=404, detail="Bank Account not found")
    db.delete(db_bankaccount)
    db.commit()