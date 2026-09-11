from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Portal de Conhecimento para Suporte Técnico",
    description="Portal para estudo de suporte técnico e DevOps",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/windows", response_class=HTMLResponse)
async def windows(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="windows.html"
    )

@app.get("/rede", response_class=HTMLResponse)
async def rede(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="rede.html"
    )