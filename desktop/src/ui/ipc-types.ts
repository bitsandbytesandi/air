export interface IPCSuccess<T> {
  success: true;
  data: T;
}

export interface IPCFailure {
  success: false;
  error: string;
}

export type IPCResponse<T> =
  | IPCSuccess<T>
  | IPCFailure;
