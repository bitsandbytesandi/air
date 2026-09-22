import type { IPCResponse } from "./ipc-types";
import { DesktopUIActions } from "./actions";

export class DesktopUIConnection {
  constructor(
    private readonly actions: DesktopUIActions,
  ) {}

  begin(): void {
    this.actions.beginConnection();
  }

  handleResponse<T>(response: IPCResponse<T>): T | null {
    if (response.success) {
      this.actions.markConnected();
      return response.data;
    }

    this.actions.fail(response.error);
    return null;
  }

  disconnect(): void {
    this.actions.markDisconnected();
  }
}
