from chat.models import Message


class ConversationContext:
    def __init__(self, max_messages: int = 50):
        if max_messages < 1:
            raise ValueError("max_messages must be at least 1.")

        self.max_messages = max_messages

    def prepare(self, messages: list[Message]) -> list[dict[str, str]]:
        selected_messages = messages[-self.max_messages:]

        if selected_messages and selected_messages[0].role == "assistant":
            selected_messages = selected_messages[1:]

        return [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in selected_messages
        ]
