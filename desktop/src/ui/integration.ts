import {
  createDesktopUIRuntime,
} from "./runtime";

export function validateDesktopUIRuntime(): void {
  const runtime = createDesktopUIRuntime();

  // Initial state
  const initial = runtime.controller.getState();

  if (initial.connection !== "disconnected") {
    throw new Error(
      "Desktop UI integration failed: initial connection state is invalid.",
    );
  }

  if (initial.chat !== "idle") {
    throw new Error(
      "Desktop UI integration failed: initial chat state is invalid.",
    );
  }

  // Input flow
  runtime.actions.updateInput("Hello AIR");

  const inputState = runtime.controller.getState();

  if (inputState.input !== "Hello AIR") {
    throw new Error(
      "Desktop UI integration failed: input state was not updated.",
    );
  }

  // Connection flow
  runtime.connection.begin();

  if (
    runtime.controller.getState().connection !== "connecting"
  ) {
    throw new Error(
      "Desktop UI integration failed: connecting state was not reached.",
    );
  }

  const successResponse = runtime.connection.handleResponse({
    success: true,
    data: {
      status: "ok",
    },
  });

  if (
    runtime.controller.getState().connection !== "connected"
  ) {
    throw new Error(
      "Desktop UI integration failed: connected state was not reached.",
    );
  }

  if (successResponse?.status !== "ok") {
    throw new Error(
      "Desktop UI integration failed: IPC success payload was not returned.",
    );
  }

  // Chat flow
  runtime.actions.beginChat();

  if (runtime.controller.getState().chat !== "sending") {
    throw new Error(
      "Desktop UI integration failed: sending state was not reached.",
    );
  }

  runtime.actions.beginStreaming();

  if (runtime.controller.getState().chat !== "streaming") {
    throw new Error(
      "Desktop UI integration failed: streaming state was not reached.",
    );
  }

  runtime.actions.completeChat();

  if (runtime.controller.getState().chat !== "completed") {
    throw new Error(
      "Desktop UI integration failed: completed state was not reached.",
    );
  }

  // Failure flow
  runtime.connection.handleResponse({
    success: false,
    error: "AIR backend unavailable.",
  });

  const errorState = runtime.controller.getState();

  if (errorState.chat !== "error") {
    throw new Error(
      "Desktop UI integration failed: error chat state was not reached.",
    );
  }

  if (errorState.error !== "AIR backend unavailable.") {
    throw new Error(
      "Desktop UI integration failed: error message was not preserved.",
    );
  }

  // Disconnect flow
  runtime.connection.disconnect();

  if (
    runtime.controller.getState().connection !== "disconnected"
  ) {
    throw new Error(
      "Desktop UI integration failed: disconnected state was not reached.",
    );
  }

  // Reset flow
  runtime.actions.reset();

  const resetState = runtime.controller.getState();

  if (
    resetState.connection !== "disconnected" ||
    resetState.chat !== "idle" ||
    resetState.input !== "" ||
    resetState.error !== null
  ) {
    throw new Error(
      "Desktop UI integration failed: reset did not restore the initial state.",
    );
  }
}
