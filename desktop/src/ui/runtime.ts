import { DesktopUIActions } from "./actions";
import { DesktopUIController } from "./controller";
import { DesktopUIStore } from "./store";

export interface DesktopUIRuntime {
  store: DesktopUIStore;
  controller: DesktopUIController;
  actions: DesktopUIActions;
}

export function createDesktopUIRuntime(): DesktopUIRuntime {
  const store = new DesktopUIStore();
  const controller = new DesktopUIController(store);
  const actions = new DesktopUIActions(controller);

  return {
    store,
    controller,
    actions,
  };
}
