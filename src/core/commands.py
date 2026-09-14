from dataclasses import dataclass


@dataclass(frozen=True)
class ChatCommand:
    content: str
    max_tokens: int = 1280
