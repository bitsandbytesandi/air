from ai.model import load_model
from chat.chat_service import ChatService
from chat.conversation import Conversation
from chat.service import ConversationService
from core.application import ApplicationService
from core.config import CONVERSATION_FILE
from storage.conversation_repository import ConversationRepository
from storage.json_repository import JsonRepository

def create_application() -> ApplicationService:
    model, tokenizer = load_model()

    conversation = Conversation()

    repository = ConversationRepository(
        JsonRepository(
            CONVERSATION_FILE
        )
    )

    conversation_service = ConversationService(
        conversation,
        repository,
    )

    chat_service = ChatService(
        conversation,
        conversation_service,
    )

    application = ApplicationService(
        chat_service,
        model,
        tokenizer,
    )

    return application
