from core.config import DATA_DIR
from core.runtime import RuntimeConfig
from storage.json_repository import JsonRepository

from .repository import SettingsRepository
from .service import SettingsService


SETTINGS_FILE = DATA_DIR / "settings.json"


def create_settings_service(
    runtime: RuntimeConfig,
) -> SettingsService:
    repository = SettingsRepository(
        JsonRepository(
            SETTINGS_FILE
        )
    )

    return SettingsService(
        repository=repository,
        runtime=runtime,
    )
