from dataclasses import dataclass

from chat.chat_service import ChatService


@dataclass
class ApplicationContext:
    chat_service: ChatService
    model: object
    tokenizer: object
