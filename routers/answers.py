from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import get_db
from app import models
from schemas import AnswerRead


router = APIRouter(prefix="/answers")


@router.get("/{answer_id}", response_model=AnswerRead)
def get_answer(answer_id: int, db: Session = Depends(get_db)):
    a = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if not a:
        raise HTTPException(status_code=404, detail="Answer not found")
    return a


@router.delete("/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    a = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if not a:
        raise HTTPException(status_code=404, detail="Answer not found")
    db.delete(a)
    db.commit()
    return None