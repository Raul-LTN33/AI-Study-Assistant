from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from utils import extract_text_from_pdf, generate_ai_content

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()

    text = extract_text_from_pdf(content)
    result = generate_ai_content(text)

    return {"result": result}