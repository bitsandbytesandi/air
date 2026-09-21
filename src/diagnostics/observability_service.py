from .observation import Observation
from .metric import Metric
from .trace import Trace
from .observability_store import ObservabilityStore


class ObservabilityService:
    def __init__(self, store: ObservabilityStore):
        self.store = store

    def record_observation(
        self,
        name: str,
        payload: dict | None = None,
    ) -> Observation:
        observation = Observation.create(name, payload)
        self.store.add_observation(observation)
        return observation

    def record_metric(
        self,
        name: str,
        value: float,
        labels: dict | None = None,
    ) -> Metric:
        metric = Metric.create(name, value, labels)
        self.store.add_metric(metric)
        return metric

    def start_trace(
        self,
        operation: str,
        metadata: dict | None = None,
    ) -> Trace:
        trace = Trace.start(operation, metadata)
        self.store.add_trace(trace)
        return trace

    def observations(self) -> list[Observation]:
        return self.store.observations()

    def metrics(self) -> list[Metric]:
        return self.store.metrics()

    def traces(self) -> list[Trace]:
        return self.store.traces()
