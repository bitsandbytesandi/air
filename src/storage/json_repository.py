import json
from pathlib import Path
from typing import Any

class JsonRepository:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def save(self, data: Any) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
   
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def load(self) -> Any:
        if not self.file_path.exists():
            return None

        with self.file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
