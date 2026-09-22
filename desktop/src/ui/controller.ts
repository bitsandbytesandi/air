import {
  DesktopUIState,
} from "./state";

import {
  DesktopUIStore,
} from "./store";

export class DesktopUIController {
  constructor(
    private readonly store: DesktopUIStore,
  ) {}

  getState(): DesktopUIState {
    return this.store.getState();
  }

  setInput(input: string): void {
    this.store.update((state) => ({
      ...state,
      input,
      error: null,
    }));
  }

  setConnectionStatus(
    status: DesktopUIState["connection"],
  ): void {
    this.store.update((state) => ({
      ...state,
      connection: status,
      error: null,
    }));
  }

  setChatStatus(
    status: DesktopUIState["chat"],
  ): void {
    this.store.update((state) => ({
      ...state,
      chat: status,
      error: null,
    }));
  }

  setError(error: string): void {
    this.store.update((state) => ({
      ...state,
      chat: "error",
      error,
    }));
  }

  reset(): void {
    this.store.reset();
  }
}
