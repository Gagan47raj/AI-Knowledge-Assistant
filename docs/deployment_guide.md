Local Deployment
uvicorn app.main:app --reload
Docker Deployment
docker build -t ai-assistant .
docker run -p 8000:8000 ai-assistant