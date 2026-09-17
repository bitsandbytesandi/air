from collections.abc import Callable
from typing import TypeAlias


ToolHandler: TypeAlias = Callable[[dict], object]
