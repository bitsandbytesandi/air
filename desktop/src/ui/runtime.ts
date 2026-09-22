import { DesktopUIActions } from "./actions";
import { DesktopUIConnection } from "./connection";
import { DesktopUIController } from "./controller";
import { DesktopUIStore } from "./store";

export interface DesktopUIRuntime {
  store: DesktopUIStore;
  controller: DesktopUIController;
  actions: DesktopUIActions;
  connection: DesktopUIConnection;
}

export function createDesktopUIRuntime(): DesktopUIRuntime {
  const store = new DesktopUIStore();
  const controller = new DesktopUIController(store);
  const actions = new DesktopUIActions(controller);
  const connection = new DesktopUIConnection(actions);

  return {
    store,
    controller,
    actions,
    connection,
  };
}
