from pathlib import Path

from storage.json_repository import JsonRepository

from .models import Settings


class SettingsRepository:
    def __init__(
        self,
        repository: JsonRepository,
    ):
        self.repository = repository

    def save(
        self,
        settings: Settings,
    ) -> None:
        self.repository.save(
            {
                "max_tokens": settings.max_tokens,
            }
        )

    def load(self) -> Settings | None:
        data = self.repository.load()

        if data is None:
            return None

        return Settings(
            max_tokens=int(
                data["max_tokens"]
            )
        )
