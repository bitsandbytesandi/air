from dataclasses import dataclass

from chat.chat_service import ChatService
from core.session import Session

@dataclass
class ApplicationContext:
    chat_service: ChatService
    model: object
    tokenizer: object
    session: Session
