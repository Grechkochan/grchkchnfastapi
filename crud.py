from sqlalchemy.orm import Session
from app import models
import schemas

def get_questions(db: Session):
    return db.query(models.Question).all()

def create_question(db: Session, q: schemas.QuestionCreate):
    question = models.Question(text=q.text)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()

def delete_question(db: Session, question_id: int):
    q = get_question(db, question_id)
    if q:
        db.delete(q)
        db.commit()
    return q

def create_answer(db: Session, question_id: int, ans: schemas.AnswerCreate):
    question = get_question(db, question_id)
    if not question:
        return None
    answer = models.Answer(**ans.dict(), question_id=question_id)
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer

def get_answer(db: Session, answer_id: int):
    return db.query(models.Answer).filter(models.Answer.id == answer_id).first()

def delete_answer(db: Session, answer_id: int):
    ans = get_answer(db, answer_id)
    if ans:
        db.delete(ans)
        db.commit()
    return ans
