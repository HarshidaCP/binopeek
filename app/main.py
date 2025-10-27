import webbrowser
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.services.bino_service import get_suggestions, generate_whatsapp_link

app = FastAPI(title="BinoPeek")

webbrowser.open("http://127.0.0.1:8000")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
   
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request, query: str = Form(...)):
    
    suggestions = get_suggestions(query)
    bino_link = generate_whatsapp_link(query)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "query": query,
            "suggestions": suggestions,
            "bino_link": bino_link,
        },
    )

