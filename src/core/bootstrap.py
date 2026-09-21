from ai.model import MODEL_PATH, load_model
from ai.model_manager import ModelManager
from tools.bootstrap import create_tool_service
from chat.chat_service import ChatService
from chat.context import ConversationContext
from chat.conversation import Conversation
from chat.service import ConversationService

from core.application import ApplicationService
from core.config import CONVERSATION_FILE
from core.context import ApplicationContext
from core.runtime import RuntimeConfig
from core.session import Session

from memory.service import MemoryService
from memory.store import MemoryStore

from storage.conversation_repository import ConversationRepository
from storage.json_repository import JsonRepository
from storage.memory_repository import MemoryRepository

from diagnostics.service import DiagnosticsService
from diagnostics.store import DiagnosticsStore
from diagnostics.health_service import HealthService
from diagnostics.health_store import HealthStore

from settings.bootstrap import create_settings_service

from events.service import ApplicationEventService
from events.store import EventStore

def create_application() -> ApplicationService:
    model, tokenizer = load_model()

    model_manager = ModelManager(
        model=model,
        model_path=MODEL_PATH,
    )

    runtime = RuntimeConfig()

    settings_service = create_settings_service(
        runtime
    )

    settings_service.restore()

    session = Session.create()

    conversation = Conversation()

    conversation_repository = ConversationRepository(
        JsonRepository(
            CONVERSATION_FILE
        )
    )

    conversation_service = ConversationService(
        conversation,
        conversation_repository,
    )

    conversation_context = ConversationContext(
        max_messages=50
    )

    chat_service = ChatService(
        conversation,
        conversation_service,
        conversation_context,
    )

    memory_store = MemoryStore()

    memory_repository = MemoryRepository(
        JsonRepository(
            CONVERSATION_FILE.parent / "memory.json"
        )
    )

    memory_service = MemoryService(
        memory_store,
        memory_repository,
    )

    tool_service = create_tool_service(
        memory_service
    )

    diagnostics_store = DiagnosticsStore()

    diagnostics_service = DiagnosticsService(
        diagnostics_store
    )

    health_store = HealthStore()

    health_service = HealthService(
        health_store
    )

    event_store = EventStore()

    event_service = ApplicationEventService(
        event_store
    )

    context = ApplicationContext(
        chat_service=chat_service,
        memory_service=memory_service,
        model=model,
        tokenizer=tokenizer,
        model_manager=model_manager,
        runtime=runtime,
        session=session,
        tool_service=tool_service,
        diagnostics_service=diagnostics_service,
        health_service=health_service,
        settings_service=settings_service,
        event_service=event_service,
    )

    return ApplicationService(
        context
    )
