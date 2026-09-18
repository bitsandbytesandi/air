from dataclasses import dataclass

from ai.model_manager import ModelManager
from chat.chat_service import ChatService
from core.runtime import RuntimeConfig
from core.session import Session
from memory.service import MemoryService
from tools.service import ToolService
from diagnostics.service import DiagnosticsService

@dataclass
class ApplicationContext:
    chat_service: ChatService
    memory_service: MemoryService
    tool_service: ToolService
    model: object
    tokenizer: object
    model_manager: ModelManager
    runtime: RuntimeConfig
    session: Session
    diagnostics_service: DiagnosticsService
