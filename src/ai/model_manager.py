from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ModelInfo:
    name: str
    path: str
    loaded: bool


class ModelManager:
    def __init__(
        self,
        model: object,
        model_path: Path,
    ):
        self._model = model
        self._model_path = model_path

    @property
    def info(self) -> ModelInfo:
        return ModelInfo(
            name=self._model_path.name,
            path=str(self._model_path),
            loaded=self._model is not None,
        )
