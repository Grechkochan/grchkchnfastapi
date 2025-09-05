from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from db import get_db
from app import models
from schemas import QuestionCreate, QuestionRead, QuestionWithAnswers, AnswerCreate, AnswerRead


router = APIRouter(prefix="/questions")


@router.get("/", response_model=list[QuestionRead])
def list_questions(db: Session = Depends(get_db)):
    items = db.query(models.Question).order_by(models.Question.id.desc()).all()
    return items


@router.post("/", response_model=QuestionRead, status_code=status.HTTP_201_CREATED)
def create_question(payload: QuestionCreate, db: Session = Depends(get_db)):
    obj = models.Question(text=payload.text)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get("/{question_id}", response_model=QuestionWithAnswers)
def get_question(question_id: int, db: Session = Depends(get_db)):
    obj = (
        db.query(models.Question)
        .options(joinedload(models.Question.answers))
        .filter(models.Question.id == question_id)
        .first()
    )
    if not obj:
        raise HTTPException(status_code=404, detail="Question not found")
    return obj


@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(obj)
    db.commit()
    return None


@router.post("/{question_id}/answers/", response_model=AnswerRead, status_code=status.HTTP_201_CREATED)
def create_answer(question_id: int, payload: AnswerCreate, db: Session = Depends(get_db)):
    q = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    a = models.Answer(question_id=question_id, user_id=payload.user_id, text=payload.text)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a