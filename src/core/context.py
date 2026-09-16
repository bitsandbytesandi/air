from dataclasses import dataclass

from ai.model_manager import ModelManager
from chat.chat_service import ChatService
from core.runtime import RuntimeConfig
from core.session import Session
from memory.service import MemoryService


@dataclass
class ApplicationContext:
    chat_service: ChatService
    memory_service: MemoryService
    model: object
    tokenizer: object
    model_manager: ModelManager
    runtime: RuntimeConfig
    session: Session
