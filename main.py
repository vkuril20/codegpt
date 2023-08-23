from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from llama_index.llms import Replicate
from llama_index.llms import ChatMessage
import os

app=FastAPI()
store={}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
os.environ["REPLICATE_API_TOKEN"] = "r8_JRFKxpkBy97VLi9ynUvVE5XHrAAJQcP455tKs"
class request(BaseModel):
    role:str
    content:str

class request_body(BaseModel):
    messages: list[request]


@app.get("/getting_data/")
async def getting_data():
    return store
    
@app.post("/posting_data/")
async def posting_data(data:request_body)->dict:
    global store
    store= data.json()
    llm = Replicate(
    model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5"
)
    messages = [
    ChatMessage(role="user", content=data.messages[1].content),
]
    resp = llm.chat(messages)
    return resp