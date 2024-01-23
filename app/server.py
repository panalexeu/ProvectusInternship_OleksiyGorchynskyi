from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_openai import ChatOpenAI

from .models import Prompt
from .utils import llm_stream_response

llm_models = dict()


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()

    llm_models['open_ai'] = ChatOpenAI()  # Setting up ChatOpenAI model before app's startup
    yield

app = FastAPI(lifespan=lifespan)


@app.post('/send-prompt', response_class=StreamingResponse)
async def send_prompt(prompt: Prompt):
    open_ai: ChatOpenAI = llm_models['open_ai']

    return StreamingResponse(
        llm_stream_response(open_ai.stream(input=prompt.content)),
        media_type='text/event-stream'
    )
