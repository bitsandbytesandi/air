from .collection import ContextCollection
from .snapshot import ContextSnapshot


class ContextSnapshotFactory:
    """Creates immutable snapshots from assembled context."""

    def create(
        self,
        collection: ContextCollection,
    ) -> ContextSnapshot:
        return ContextSnapshot(
            items=tuple(collection.get_all()),
        )
