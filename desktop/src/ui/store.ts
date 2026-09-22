import {
  DesktopUIState,
  initialDesktopUIState,
} from "./state";

export class DesktopUIStore {
  private state: DesktopUIState;

  constructor(
    initialState: DesktopUIState = initialDesktopUIState,
  ) {
    this.state = { ...initialState };
  }

  getState(): DesktopUIState {
    return { ...this.state };
  }

  setState(nextState: DesktopUIState): void {
    this.state = { ...nextState };
  }

  update(
    updater: (
      state: DesktopUIState,
    ) => DesktopUIState,
  ): void {
    this.state = updater(this.getState());
  }

  reset(): void {
    this.state = {
      ...initialDesktopUIState,
    };
  }
}
