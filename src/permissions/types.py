from enum import Enum


class PermissionAction(str, Enum):
    DISCOVER = "discover"
    EXECUTE = "execute"
    READ = "read"
    WRITE = "write"
    DELETE = "delete"


class PermissionDecision(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
