from enum import Enum


class ToolRiskLevel(str, Enum):
    SAFE = "safe"
    CONTROLLED = "controlled"
    RESTRICTED = "restricted"
