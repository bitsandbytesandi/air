export type ConnectionStatus =
  | "disconnected"
  | "connecting"
  | "connected"
  | "error";

export type ChatStatus =
  | "idle"
  | "sending"
  | "streaming"
  | "completed"
  | "error";

export interface DesktopUIState {
  connection: ConnectionStatus;
  chat: ChatStatus;
  input: string;
  error: string | null;
}

export const initialDesktopUIState: DesktopUIState = {
  connection: "disconnected",
  chat: "idle",
  input: "",
  error: null,
};
