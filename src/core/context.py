from dataclasses import dataclass

from ai.model_manager import ModelManager
from chat.chat_service import ChatService
from core.runtime import RuntimeConfig
from core.session import Session
from memory.service import MemoryService
from tools.service import ToolService
from diagnostics.service import DiagnosticsService
from diagnostics.health_service import HealthService
from settings.service import SettingsService
from events.service import ApplicationEventService

@dataclass
class ApplicationContext:
    chat_service: ChatService
    memory_service: MemoryService
    tool_service: ToolService
    diagnostics_service: DiagnosticsService
    health_service: HealthService
    model: object
    tokenizer: object
    model_manager: ModelManager
    runtime: RuntimeConfig
    session: Session
    settings_service: SettingsService
    event_service: ApplicationEventService
