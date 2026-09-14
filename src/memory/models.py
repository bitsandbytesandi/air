from dataclasses import dataclass
from datetime import datetime

@dataclass
class Memory:
    content: str
    created_at: datetime
