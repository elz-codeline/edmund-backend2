from fastapi import FastAPI
from pydantic import BaseModel

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

app = FastAPI()

@app.get("/maths") # this is an endpoint
def calculation():

    answer = 1 + 1

    return {"answer": answer}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(response=answer)