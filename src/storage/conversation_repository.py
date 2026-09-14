from datetime import datetime
from chat.conversation import Conversation
from chat.models import Message
from .json_repository import JsonRepository

class ConversationRepository:
    def __init__(self, repository: JsonRepository):
        self.repository = repository

    def save(self, conversation: Conversation) -> None:
        data = {
            "messages": [
                {
                    "role": message.role,
                    "content": message.content,
                    "created_at": message.created_at.isoformat(),
                }
                for message in conversation.messages
                
            ]
        }

        self.repository.save(data)

    def load(self) -> Conversation | None:
        data = self.repository.load()

        if data is None:
            return None

        conversation = Conversation()

        for item in data["messages"]:
            message = Message(
                role=item["role"],
                content=item["content"],
                created_at=datetime.fromisoformat(item["created_at"]),
            )

            conversation.add_message(message)

        return conversation
