import {
  airMemories,
  airRemember,
  airSearchMemories,
  type MemoryListResponse,
  type MemoryResponse,
} from "./ipc";


export class MemoryClient {
  async list(): Promise<MemoryListResponse> {
    return airMemories();
  }

  async search(
    query: string,
  ): Promise<MemoryListResponse> {
    return airSearchMemories(
      query.trim(),
    );
  }


  async remember(
    content: string,
  ): Promise<MemoryResponse> {
    const normalizedContent =
      content.trim();

    if (!normalizedContent) {
      throw new Error(
        "Memory content cannot be empty.",
      );
    }

    return airRemember(
      normalizedContent,
    );
  }
}
