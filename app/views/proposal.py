from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.proposal import ProposalSchema
from app.controllers import proposal as proposal_controller

router = APIRouter()

@router.post("/", response_model=ProposalSchema)
def create_proposal_view(proposal: ProposalSchema, db: Session = Depends(get_db)):
    return proposal_controller.create_proposal(db=db, proposal=proposal)

@router.get("/{proposal_id}", response_model=ProposalSchema)
def read_proposal(proposal_id: str, db: Session = Depends(get_db)):
    db_proposal = proposal_controller.get_proposal(db, proposal_id=proposal_id)
    if db_proposal is None:
        raise HTTPException(status_code=404, detail="Proposal not found")
    return db_proposal

@router.put("/{proposal_id}", response_model=ProposalSchema)
def update_proposal_view(proposal_id: str, proposal: ProposalSchema, db: Session = Depends(get_db)):
    return proposal_controller.update_proposal(db=db, proposal_id=proposal_id, proposal=proposal)

@router.delete("/{proposal_id}")
def delete_proposal_view(proposal_id: str, db: Session = Depends(get_db)):
    return proposal_controller.delete_proposal(db=db, proposal_id=proposal_id)