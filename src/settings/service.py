from core.runtime import RuntimeConfig

from .models import Settings
from .repository import SettingsRepository
from .validation import SettingsValidator


class SettingsService:
    def __init__(
        self,
        repository: SettingsRepository,
        runtime: RuntimeConfig,
        validator: SettingsValidator | None = None,
    ):
        self.repository = repository
        self.runtime = runtime
        self.validator = (
            validator
            or SettingsValidator()
        )

    def current(self) -> Settings:
        return Settings(
            max_tokens=self.runtime.max_tokens
        )

    def update(
        self,
        settings: Settings,
    ) -> Settings:
        self.validator.validate(settings)

        self.runtime.set_max_tokens(
            settings.max_tokens
        )

        self.repository.save(settings)

        return settings

    def restore(self) -> Settings:
        settings = self.repository.load()

        if settings is None:
            settings = self.current()
            self.repository.save(settings)
            return settings

        self.validator.validate(settings)

        self.runtime.set_max_tokens(
            settings.max_tokens
        )

        return settings
