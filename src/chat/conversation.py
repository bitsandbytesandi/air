from dataclasses import dataclass, field
from .models import Message

@dataclass
class Conversation:
    messages: list[Message] = field(default_factory=list)

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    def to_chat_messages(self) -> list[dict[str, str]]:
        return [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in self.messages
        ]
