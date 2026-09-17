from dataclasses import dataclass

@dataclass(frozen=True)
class Tool:
    id: str
    name: str
    description: str
    input_schema: dict
