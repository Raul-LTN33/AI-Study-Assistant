import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def extract_text_from_pdf(file_bytes):
    reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def generate_ai_content(text):
    prompt = f"""
    Ești un generator strict de conținut educațional.

    REGULI OBLIGATORII:
    - Nu adăuga conversații, comentarii sau propoziții către utilizator.
    - Nu adăuga introduceri sau concluzii.
    - Respectă EXACT formatul cerut.
    - Dacă nu respecți formatul, răspunsul este invalid.

    STRUCTURĂ:

    1. REZUMAT (300-500 de cuvinte)

    2. ÎNTREBĂRI GRILĂ
    - Generează EXACT 10 întrebări
    - Fiecare întrebare are 4 variante (a, b, c, d)
    - Indică răspunsul corect
    - Numerotare de la 1 la 10

    3. ÎNTREBĂRI DESCHISE
    - Generează EXACT 5 întrebări
    - Numerotare de la 1 la 5 


    Text:
    {text[:8000]}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content