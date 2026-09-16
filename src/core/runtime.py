from dataclasses import dataclass

DEFAULT_MAX_TOKENS = 512
MIN_MAX_TOKENS = 1
MAX_MAX_TOKENS = 8192

@dataclass
class RuntimeConfig:
    max_tokens: int = DEFAULT_MAX_TOKENS

    def __post_init__(self) -> None:
        self.set_max_tokens(self.max_tokens)

    def set_max_tokens(
        self,
        value: int,
    ) -> None:
        if not isinstance(value, int):
            raise TypeError(
                "max_tokens must be an integer."
            )

        if not (
            MIN_MAX_TOKENS
            <= value
            <= MAX_MAX_TOKENS
        ):
            raise ValueError(
                "max_tokens must be between "
                f"{MIN_MAX_TOKENS} and "
                f"{MAX_MAX_TOKENS}."
            )
    
        self.max_tokens = value
           
