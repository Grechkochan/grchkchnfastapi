from pydantic import BaseModel, ConfigDict, constr
from datetime import datetime

class QuestionCreate(BaseModel):
    text: constr(min_length=1, strip_whitespace=True)


class QuestionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    text: str
    created_at: datetime


class AnswerCreate(BaseModel):
    user_id: constr(min_length=1)
    text: constr(min_length=1, strip_whitespace=True)


class AnswerRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    question_id: int
    user_id: str
    text: str
    created_at: datetime

class QuestionWithAnswers(QuestionRead):
    answers: list[AnswerRead] = []