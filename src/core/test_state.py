from core.state import ApplicationState

assert ApplicationState.CREATED.value == "created"
assert ApplicationState.STARTING.value == "starting"
assert ApplicationState.RUNNING.value == "running"
assert ApplicationState.STOPPING.value == "stopping"
assert ApplicationState.STOPPED.value == "stopped"
assert ApplicationState.FAILED.value == "failed"

print("Brick 31 - Application state: GREEN")

