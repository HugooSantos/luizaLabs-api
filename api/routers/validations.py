from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.services import validations_service
from api.shared.dependencies import get_db

router = APIRouter()

@router.get("/ean/{ean}", status_code=204)
def validate_ean(ean: str, db: Session = Depends(get_db)):    
    validations_service.validate_ean(ean=ean, db=db)