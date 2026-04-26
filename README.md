# AI Study Assistant

## Scopul proiectului

Scopul acestui proiect este de a automatiza procesul de studiu prin generarea de conținut educațional structurat din fișiere PDF. Aplicația extrage text din documente și folosește un model de inteligență artificială pentru a crea rezumate, întrebări grilă și întrebări deschise, cu scopul de a facilita învățarea și înțelegerea materialelor.

## Funcționalități

- Extragerea textului din fișiere PDF
- Generarea de rezumate automate pe baza textului extras
- Generarea de întrebări grilă cu variante de răspuns și indicarea răspunsului corect
- Generarea de întrebări deschise pentru aprofundarea conținutului
- Integrare cu OpenAI API pentru procesarea și generarea de conținut

## Tehnologii folosite

- Python
- OpenAI API (GPT-4.1-mini)
- PyPDF2
- python-dotenv
- Git și GitHub

## Rulare proiect

1. Clonează repository-ul
   git clone https://github.com/Raul-LTN33/AI-Study-Assistant

2. Instalează dependințele
   pip install -r requirements.txt

3. Creează fișierul .env și adaugă cheia API
   OPENAI_API_KEY=cheia_ta_api

4. Rulează aplicația
   python main.py

## Securitate

Cheia API este stocată în variabile de mediu și nu este inclusă în codul sursă. Fișierul .env este exclus din repository prin .gitignore.

## Autor

<<<<<<< HEAD
Proiect realizat în scop educațional pentru automatizarea procesului de studiu folosind inteligență artificială.
=======
Proiect realizat în scop educațional pentru automatizarea procesului de studiu folosind inteligență artificială.
>>>>>>> 8477cdc (Versiunea 1.0)
