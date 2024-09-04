from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.bankaccount import BankAccountSchema
from app.controllers import bankaccount as bankaccount_controller

router = APIRouter()

@router.post("/", response_model=BankAccountSchema)
def create_bankaccount_view(bankaccount: BankAccountSchema, db: Session = Depends(get_db)):
    return bankaccount_controller.create_bankaccount(db=db, bankaccount=bankaccount)

@router.get("/{bankaccount_id}", response_model=BankAccountSchema)
def read_bankaccount(bankaccount_id: str, db: Session = Depends(get_db)):
    db_bankaccount = bankaccount_controller.get_bankaccount(db, bankaccount_id=bankaccount_id)
    if db_bankaccount is None:
        raise HTTPException(status_code=404, detail="Bankaccount not found")
    return db_bankaccount

@router.put("/{bankaccount_id}", response_model=BankAccountSchema)
def update_bankaccount_view(bankaccount_id: str, bankaccount: BankAccountSchema, db: Session = Depends(get_db)):
    return bankaccount_controller.update_bankaccount(db=db, bankaccount_id=bankaccount_id, bankaccount=bankaccount)

@router.delete("/{bankaccount_id}")
def delete_bankaccount_view(bankaccount_id: str, db: Session = Depends(get_db)):
    return bankaccount_controller.delete_bankaccount(db=db, bankaccount_id=bankaccount_id)