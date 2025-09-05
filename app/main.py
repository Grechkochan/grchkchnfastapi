from fastapi import FastAPI
from routers import questions, answers

app = FastAPI(title="Q&A API")

app.include_router(questions.router)
app.include_router(answers.router)
