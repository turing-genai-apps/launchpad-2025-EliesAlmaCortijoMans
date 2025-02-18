from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .agent import ConversationAgent

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

conversation_agent = ConversationAgent()

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = conversation_agent.process_message(request.message)
    return ChatResponse(response=response)