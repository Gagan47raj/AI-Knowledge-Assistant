POST /api/v1/ask
Request
{
  "question":"What is FastAPI?"
}
Response
{
  "request_id":"uuid",
  "question":"What is FastAPI?",
  "answer":"...",
  "confidence":91.2,
  "hallucination_risk":"low",
  "sources":[
      "knowledge.txt"
  ],
  "execution_time":0.78
}
GET /health
Response
{
  "status":"healthy"
}