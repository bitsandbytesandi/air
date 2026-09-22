import { DesktopUIController } from "./controller";

export class DesktopUIActions {
  constructor(
    private readonly controller: DesktopUIController,
  ) {}

  updateInput(input: string): void {
    this.controller.setInput(input);
  }

  beginConnection(): void {
    this.controller.setConnectionStatus("connecting");
  }

  markConnected(): void {
    this.controller.setConnectionStatus("connected");
  }

  markDisconnected(): void {
    this.controller.setConnectionStatus("disconnected");
  }

  beginChat(): void {
    this.controller.setChatStatus("sending");
  }

  beginStreaming(): void {
    this.controller.setChatStatus("streaming");
  }

  completeChat(): void {
    this.controller.setChatStatus("completed");
  }

  fail(error: string): void {
    this.controller.setError(error);
  }

  reset(): void {
    this.controller.reset();
  }
}
