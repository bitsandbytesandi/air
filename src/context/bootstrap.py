from .assembly import ContextAssembly
from .provider_collection import ContextProviderCollection
from .service import ContextService
from .snapshot_factory import ContextSnapshotFactory


class ContextSystem:
    """Composes the context subsystem."""

    def __init__(
        self,
        provider_collection: ContextProviderCollection,
        service: ContextService,
        snapshot_factory: ContextSnapshotFactory,
    ):
        self.provider_collection = provider_collection
        self.service = service
        self.snapshot_factory = snapshot_factory

    def build_snapshot(self):
        collection = self.service.build(
            self.provider_collection.get_all()
        )

        return self.snapshot_factory.create(collection)


def create_context_system() -> ContextSystem:
    """Create the default context subsystem."""

    provider_collection = ContextProviderCollection()
    assembly = ContextAssembly()
    service = ContextService(assembly)
    snapshot_factory = ContextSnapshotFactory()

    return ContextSystem(
        provider_collection=provider_collection,
        service=service,
        snapshot_factory=snapshot_factory,
    )
