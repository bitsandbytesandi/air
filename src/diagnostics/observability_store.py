from .observation import Observation
from .metric import Metric
from .trace import Trace


class ObservabilityStore:
    def __init__(self):
        self._observations: list[Observation] = []
        self._metrics: list[Metric] = []
        self._traces: list[Trace] = []

    def add_observation(self, observation: Observation) -> None:
        self._observations.append(observation)

    def add_metric(self, metric: Metric) -> None:
        self._metrics.append(metric)

    def add_trace(self, trace: Trace) -> None:
        self._traces.append(trace)

    def observations(self) -> list[Observation]:
        return list(self._observations)

    def metrics(self) -> list[Metric]:
        return list(self._metrics)

    def traces(self) -> list[Trace]:
        return list(self._traces)

    def clear(self) -> None:
        self._observations.clear()
        self._metrics.clear()
        self._traces.clear()
