from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.proposal import Proposal
from app.schemas.proposal import ProposalSchema

def get_proposal(db: Session, proposal_id: str):
    return db.query(Proposal).filter(Proposal.id == proposal_id).first()

def create_proposal(db: Session, proposal: ProposalSchema):
    db_proposal = Proposal(id=proposal.id, farmer_id=proposal.farmer_id, type=proposal.type, weight=proposal.weight, quality=proposal.quality)
    db.add(db_proposal)
    db.commit()
    db.refresh(db_proposal)
    return db_proposal

def update_proposal(db: Session, proposal_id: str, proposal: ProposalSchema):
    db_proposal = get_proposal(db, proposal_id)
    if not db_proposal:
        raise HTTPException(status_code=404, detail="Proposal not found")
    db_proposal.farmer_id = proposal.farmer_id
    db_proposal.type = proposal.type
    db_proposal.weight = proposal.weight
    db_proposal.quality = proposal.quality
    db.commit()
    db.refresh(db_proposal)
    return db_proposal

def delete_proposal(db: Session, proposal_id: str):
    db_proposal = get_proposal(db, proposal_id)
    if not db_proposal:
        raise HTTPException(status_code=404, detail="Proposal not found")
    db.delete(db_proposal)
    db.commit()