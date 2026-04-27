from pydantic import BaseModel, constr

class ChatMessage(BaseModel):
    user: str
    message: str