import {
  airDeleteMemory,
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

  async delete(
    id: string,
  ): Promise<void> {
    const normalizedId =
      id.trim();

    if (!normalizedId) {
      throw new Error(
        "Memory ID cannot be empty.",
      );
    }

    await airDeleteMemory(
      normalizedId,
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
