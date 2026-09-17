import { invoke } from "@tauri-apps/api/core";


export interface HealthResponse {
  status: string;
  application: string;
}


export interface ConversationMessage {
  role: string;
  content: string;
  created_at: string;
}


export interface ConversationResponse {
  messages: ConversationMessage[];
}


export interface ChatResponse {
  content: string;
}


export interface ModelInfo {
  name: string;
  path: string;
  loaded: boolean;
}


export interface RuntimeConfig {
  max_tokens: number;
}


export interface RuntimeResponse {
  status: string;
  application: string;
  model: ModelInfo;
  config: RuntimeConfig;
}


/*
 * Memory
 */

export interface MemoryResponse {
  content: string;
  created_at: string;
}


export interface MemoryListResponse {
  memories: MemoryResponse[];
}


export async function airHealth(): Promise<HealthResponse> {
  return invoke<HealthResponse>(
    "air_health",
  );
}


export async function airConversation(): Promise<ConversationResponse> {
  return invoke<ConversationResponse>(
    "air_conversation",
  );
}


export async function airChat(
  content: string,
  maxTokens?: number,
): Promise<ChatResponse> {
  return invoke<ChatResponse>(
    "air_chat",
    {
      content,
      max_tokens: maxTokens,
    },
  );
}


export async function airRuntime(): Promise<RuntimeResponse> {
  return invoke<RuntimeResponse>(
    "air_runtime",
  );
}


/*
 * Memory IPC
 */

export async function airMemories(): Promise<MemoryListResponse> {
  return invoke<MemoryListResponse>(
    "air_memories",
  );
}

export async function airSearchMemories(
  query: string,
): Promise<MemoryListResponse> {
  return invoke<MemoryListResponse>(
    "air_search_memories",
    {
      query,
    },
  );
}

export async function airRemember(
  content: string,
): Promise<MemoryResponse> {
  return invoke<MemoryResponse>(
    "air_remember",
    {
      content,
    },
  );
}
