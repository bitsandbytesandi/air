from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    max_tokens: int
