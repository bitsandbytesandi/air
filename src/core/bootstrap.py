from ai.model import load_model

from chat.chat_service import ChatService
from chat.context import ConversationContext
from chat.conversation import Conversation
from chat.service import ConversationService

from core.application import ApplicationService
from core.config import CONVERSATION_FILE
from core.context import ApplicationContext
from core.session import Session

from storage.conversation_repository import ConversationRepository
from storage.json_repository import JsonRepository


def create_application() -> ApplicationService:
    model, tokenizer = load_model()

    session = Session.create()

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

    conversation_context = ConversationContext(
        max_messages=50
    )

    chat_service = ChatService(
        conversation,
        conversation_service,
        conversation_context,
    )

    context = ApplicationContext(
        chat_service=chat_service,
        model=model,
        tokenizer=tokenizer,
        session=session,
    )

    return ApplicationService(
        context
    )
