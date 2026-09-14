from .conversation import Conversation
from .models import Message
from storage.conversation_repository import ConversationRepository

class ConversationService:
    def __init__(
        self,
        conversation: Conversation,
        repository: ConversationRepository,
    ):
        self.conversation = conversation
        self.repository = repository

    def add_message(self, role: str, content: str) -> Message:
        from datetime import datetime

        message = Message(
            role=role,
            content=content,
            created_at=datetime.now(),
        )
 
        self.conversation.add_message(message)
        self.repository.save(self.conversation)

        return message
    
    def load(self) -> Conversation | None:
        return self.repository.load()

    def get_messages(self) -> list[Message]:
        return list(self.conversation.messages)
