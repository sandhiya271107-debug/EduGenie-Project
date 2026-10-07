from fastapi import (
    FastAPI,
    HTTPException,
    Request
)

from fastapi.responses import HTMLResponse

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates


from schemas import TaskRequest

from qna import answer_question

from explanation_module import explain_concept

from quiz_module import generate_quiz

from summary_module import summarize_text

from learning_path import (
    get_learning_recommendations
)


app = FastAPI(

    title="EduGenie",

    version="1.0.0",

    description=(
        "Google Gemini powered "
        "learning assistant"
    )
)


app.mount(
    "/static",
    StaticFiles(
        directory="static"
    ),
    name="static"
)


templates = Jinja2Templates(
    directory="templates"
)


@app.get("/",
    response_class=HTMLResponse
)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )
    
@app.get("/health")
async def health():

    return {
        "status": "ok",
        "service": "EduGenie"
    }


@app.post("/qa")
async def qa(
    payload: TaskRequest
):

    if not payload.text.strip():

        raise HTTPException(
            status_code=400,
            detail="Please enter a question."
        )

    try:

        result = answer_question(
            payload.text
        )

        return {
            "result": result
        }

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc)
        ) from exc


@app.post("/explain")
async def explain(
    payload: TaskRequest
):

    if not payload.text.strip():

        raise HTTPException(
            status_code=400,
            detail="Please enter a topic."
        )

    try:

        result = explain_concept(
            payload.text
        )

        return {
            "result": result
        }

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc)
        ) from exc


@app.post("/quiz")
async def quiz(
    payload: TaskRequest
):

    if not payload.text.strip():

        raise HTTPException(
            status_code=400,
            detail="Please enter a topic."
        )

    try:

        return generate_quiz(
            payload.text
        )

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc)
        ) from exc


@app.post("/summarize")
async def summarize(
    payload: TaskRequest
):

    if not payload.text.strip():

        raise HTTPException(
            status_code=400,
            detail=(
                "Please enter text "
                "to summarize."
            )
        )

    try:

        result = summarize_text(
            payload.text
        )

        return {
            "result": result
        }

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc)
        ) from exc


@app.post(
    "/learn/recommendations"
)
async def learning_recommendations(
    payload: TaskRequest
):

    if not payload.text.strip():

        raise HTTPException(
            status_code=400,
            detail="Please enter a topic."
        )

    try:

        result = get_learning_recommendations(
            payload.text
        )

        return {
            "result": result
        }

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc)
        ) from exc