Clone Project
git clone <repo>
Create Virtual Environment
python -m venv venv
Activate
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Run Ollama
ollama run mistral
Start FastAPI
uvicorn app.main:app --reload