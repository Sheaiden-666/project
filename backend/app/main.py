from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from qr_generator import generate_qr_base64

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("app/static/index.html", "r", encoding="utf-8") as file:
        return file.read()


@app.post("/generate")
async def generate_qr(text: str = Form(...)):
    qr_code = generate_qr_base64(text)

    return {
        "qr": qr_code
    }
    