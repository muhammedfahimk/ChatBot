# from fastapi import FastAPI, Request, Form
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

# from models import ChatMessage

# app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")

# chat_messages = [
#     ChatMessage(user="AI", message="Hello!"),
#     ChatMessage(user="user", message="Please call me Fahim."),
#     ChatMessage(user="AI", message="Will do. How can I help you?"),
# ]


# @app.get("/", response_class=HTMLResponse)
# def index(request: Request) -> HTMLResponse:
#     return templates.TemplateResponse(
#         request,
#         "index.html",
#         {"chat_messages": chat_messages}
#     )


# @app.post("/ask-ai", response_class=HTMLResponse)
# def ask_ai(request: Request, message: str = Form(...)) -> HTMLResponse:
#     chat_messages.append(ChatMessage(user="user", message=message))

#     return templates.TemplateResponse(
#         request,
#         "chat-messages.html",
#         {"chat_messages": chat_messages}
#     )




from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from google import genai
import os

from models import ChatMessage

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat_messages = [
    ChatMessage(user="AI", message="Hello! How can I help you?")
]


def get_ai_reply(message: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    global chat_messages
    chat_messages = [
        ChatMessage(user="AI", message="Hello! How can I help you?")
    ]

    return templates.TemplateResponse(
        request,
        "index.html",
        {"chat_messages": chat_messages}
    )


@app.post("/ask-ai", response_class=HTMLResponse)
def ask_ai(request: Request, message: str = Form(...)) -> HTMLResponse:
    chat_messages.append(ChatMessage(user="user", message=message))

    bot_reply = get_ai_reply(message)

    chat_messages.append(ChatMessage(user="AI", message=bot_reply))

    return templates.TemplateResponse(
        request,
        "chat-messages.html",
        {"chat_messages": chat_messages}
    )