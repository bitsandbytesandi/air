from core.runtime import (
    MAX_MAX_TOKENS,
    MIN_MAX_TOKENS,
)

from .models import Settings


class SettingsValidator:
    def validate(
        self,
        settings: Settings,
    ) -> None:
        if not isinstance(
            settings.max_tokens,
            int,
        ):
            raise TypeError(
                "max_tokens must be an integer."
            )

        if not (
            MIN_MAX_TOKENS
            <= settings.max_tokens
            <= MAX_MAX_TOKENS
        ):
            raise ValueError(
                "max_tokens must be between "
                f"{MIN_MAX_TOKENS} and "
                f"{MAX_MAX_TOKENS}."
            )
