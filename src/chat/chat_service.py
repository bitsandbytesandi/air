from core.errors import ApplicationError
from chat.context import ConversationContext
from chat.conversation import Conversation
from chat.service import ConversationService
from ai.prompting import build_conversation_prompt
from ai.generation import generate_response

class ChatService:
    def __init__(
        self,
        conversation: Conversation,
        conversation_service: ConversationService,
        context: ConversationContext,
    ):
        self.conversation = conversation
        self.conversation_service = conversation_service
        self.context = context

    def receive_message(self, content: str) -> None:
        self.conversation_service.add_message(
            role="user",
            content=content,
        )

    def build_prompt(self, tokenizer) -> str:
        messages = self.context.prepare(
            self.conversation.messages
        )

        return build_conversation_prompt(
            tokenizer,
            messages,
        )

    def generate_reply(self, model, tokenizer, max_tokens=None) -> str:
        prompt = self.build_prompt(tokenizer)

        response = generate_response(
            model,
            tokenizer,
            prompt,
            max_tokens=max_tokens,
        )

        if not response:
            raise ApplicationError(
                "AI returned an empty response."
            )

        self.conversation_service.add_message(
            role="assistant",
            content=response,
        )

        return response

    def chat(
        self,
        content: str,
        model,
        tokenizer,
        max_tokens=None,
    ) -> str:
        self.receive_message(content)
    
        return self.generate_reply(
            model,
            tokenizer,
            max_tokens=max_tokens,
        )
          
    def restore(self) -> None:
        restored = self.conversation_service.load()

        if restored is None:
            return

        self.conversation.messages = restored.messages

    def get_messages(self):
        return self.conversation_service.get_messages()

