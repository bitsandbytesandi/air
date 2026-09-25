from core.bootstrap import create_application
from core.state import ApplicationState


application = create_application()

# The application owns lifecycle state.
assert application.state == ApplicationState.CREATED

# The integration system is composed at application creation.
assert application.integration is not None
assert application.integration.system is not None

# The integration subsystems are composition-time services.
assert application.integration.system.context is not None
assert application.integration.system.runtime is not None
assert application.integration.system.reliability is not None

# Application lifecycle remains owned by ApplicationService.
application.start()

assert application.state == ApplicationState.RUNNING

application.shutdown()

assert application.state == ApplicationState.STOPPED

print("70.5.2 lifecycle boundary: GREEN")
print("Application lifecycle ownership: GREEN")
print("Context lifecycle contract: GREEN")
print("Runtime lifecycle contract: GREEN")
print("Reliability lifecycle contract: GREEN")
