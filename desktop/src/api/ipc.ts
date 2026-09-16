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

export async function airHealth(): Promise<HealthResponse> {
  return invoke<HealthResponse>("air_health");
}

export async function airConversation(): Promise<ConversationResponse> {
  return invoke<ConversationResponse>("air_conversation");
}

export async function airChat(
  content: string,
  maxTokens?: number,
): Promise<ChatResponse> {
  return invoke<ChatResponse>("air_chat", {
    content,
    max_tokens: maxTokens,
  });
}
