from dataclasses import dataclass

from context.bootstrap import (
    ContextSystem,
    create_context_system,
)

from runtime.bootstrap import (
    RuntimeSystem,
    create_runtime_system,
)

from reliability.boundary import RecoveryBoundary


@dataclass
class AIRSystem:
    """
    Top-level composition root for AIR.

    This class owns system composition only.
    Individual subsystems retain their own responsibilities.
    """

    context: ContextSystem
    runtime: RuntimeSystem
    reliability: RecoveryBoundary


def create_air_system() -> AIRSystem:
    """
    Create the core AIR integration system.
    """

    context = create_context_system()
    runtime = create_runtime_system()
    reliability = RecoveryBoundary()

    return AIRSystem(
        context=context,
        runtime=runtime,
        reliability=reliability,
    )
