from dataclasses import dataclass

from ai.model_manager import ModelManager
from chat.chat_service import ChatService
from core.session import Session
from core.runtime import RuntimeConfig

@dataclass
class ApplicationContext:
    chat_service: ChatService
    model: object
    tokenizer: object
    model_manager: ModelManager
    runtime: RuntimeConfig
    session: Session
