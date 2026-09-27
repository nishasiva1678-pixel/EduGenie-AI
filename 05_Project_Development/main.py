from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


app = FastAPI(title="EduGenie")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(
    directory="templates"
)


class UserInput(BaseModel):
    task: str
    text: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)


@app.post("/api/generate")
async def generate(data: UserInput):

    task = data.task
    text = data.text.strip()

    if not text:
        return {
            "result": "Please enter some text."
        }

    if task == "qna":
        result = answer_question(text)

    elif task == "explain":
        result = explain_topic(text)

    elif task == "quiz":
        result = generate_quiz(text)

    elif task == "summary":
        result = summarize_text(text)

    elif task == "learning":
        result = get_learning_recommendations(text)

    else:
        result = "Invalid task selected."

    return {
        "result": result
    }