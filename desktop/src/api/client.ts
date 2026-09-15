const AIR_API_URL =
  import.meta.env.VITE_AIR_API_URL ??
  "http://127.0.0.1:8000";

const AIR_API_TOKEN =
  import.meta.env.VITE_AIR_API_TOKEN ?? "";

export interface ChatRequest {
  content: string;
  max_tokens?: number;
}

export interface ChatResponse {
  content: string;
}

export interface ConversationMessage {
  role: string;
  content: string;
  created_at: string;
}

export interface ConversationResponse {
  messages: ConversationMessage[];
}

export class AirClient {
  private readonly baseUrl: string;
  private readonly token: string;

  constructor(
    baseUrl = AIR_API_URL,
    token = AIR_API_TOKEN,
  ) {
    this.baseUrl = baseUrl;
    this.token = token;
  }

  private headers(): HeadersInit {
    return {
      Authorization: `Bearer ${this.token}`,
      "Content-Type": "application/json",
    };
  }

  async health(): Promise<unknown> {
    const response = await fetch(
      `${this.baseUrl}/v1/health`,
      {
        headers: this.headers(),
      },
    );

    if (!response.ok) {
      throw new Error(
        `AIR health request failed: ${response.status}`,
      );
    }

    return response.json();
  }

  async chat(
    request: ChatRequest,
  ): Promise<ChatResponse> {
    const response = await fetch(
      `${this.baseUrl}/v1/chat`,
      {
        method: "POST",
        headers: this.headers(),
        body: JSON.stringify(request),
      },
    );

    if (!response.ok) {
      throw new Error(
        `AIR chat request failed: ${response.status}`,
      );
    }

    return response.json();
  }

  async conversation(): Promise<ConversationResponse> {
    const response = await fetch(
      `${this.baseUrl}/v1/conversation`,
      {
        headers: this.headers(),
      },
    );

    if (!response.ok) {
      throw new Error(
        `AIR conversation request failed: ${response.status}`,
      );
    }

    return response.json();
  }
}
