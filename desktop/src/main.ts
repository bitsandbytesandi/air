import "./styles.css";

import {
  airConversation,
  airHealth,
  airRuntime,
  type ConversationMessage,
  type RuntimeResponse,
  type MemoryResponse,
} from "./api/ipc";

import {
  AirClient,
} from "./api/client";

import {
  MemoryClient,
} from "./api/memory";


const client = new AirClient();
const memoryClient = new MemoryClient();


const app =
  document.querySelector<HTMLDivElement>("#app");

if (!app) {
  throw new Error(
    "AIR application root was not found.",
  );
}


app.innerHTML = `
  <main class="air-shell">

    <header class="air-header">
      <div>
        <h1>AIR</h1>
        <p>Artificial Intelligence Runtime</p>
      </div>

      <div
        id="status"
        class="status"
      >
        Connecting...
      </div>
    </header>


    <section class="model-panel">

      <div class="model-panel-header">

        <div>
          <span class="panel-label">
            MODEL CONTROL
          </span>

          <h2 id="model-name">
            Loading model...
          </h2>
        </div>

        <div
          id="model-status"
          class="status-badge"
        >
          Loading...
        </div>

      </div>


      <div class="model-panel-grid">

        <div class="model-stat">
          <span class="model-stat-label">
            Application
          </span>

          <strong id="application-status">
            Loading...
          </strong>
        </div>


        <div class="model-stat">
          <span class="model-stat-label">
            Model loaded
          </span>

          <strong id="model-loaded">
            Loading...
          </strong>
        </div>


        <div class="model-stat">
          <span class="model-stat-label">
            Max tokens
          </span>

          <strong id="runtime-max-tokens">
            Loading...
          </strong>
        </div>

      </div>


      <div class="model-path">
        <span class="model-stat-label">
          Model path
        </span>

        <code id="model-path">
          Loading...
        </code>
      </div>


      <button
        id="refresh-runtime-button"
        type="button"
      >
        Refresh runtime
      </button>

    </section>


    <!-- MEMORY PANEL -->

    <section class="memory-panel">

      <div class="memory-panel-header">

        <div>
          <span class="panel-label">
            MEMORY
          </span>

          <h2>
            AIR Memory
          </h2>

          <p class="memory-description">
            Persistent information stored by AIR.
          </p>
        </div>

        <button
          id="refresh-memory-button"
          type="button"
        >
          Refresh memory
        </button>

      </div>


      <form
        id="memory-form"
        class="memory-form"
      >

        <label
          for="memory-input"
          class="memory-input-label"
        >
          Remember something
        </label>

        <textarea
          id="memory-input"
          rows="3"
          maxlength="10000"
          placeholder="Enter information AIR should remember..."
        ></textarea>

        <div class="memory-form-footer">

          <span
            id="memory-character-count"
            class="memory-character-count"
          >
            0 / 10000
          </span>

          <button
            id="remember-button"
            type="submit"
          >
            Remember
          </button>

        </div>

      </form>
 
      <div class="memory-search">

        <label
          for="memory-search-input"
          class="memory-input-label"
        >
          Search memories
        </label>

        <div class="memory-search-row">

          <input
            id="memory-search-input"
            type="search"
            placeholder="Search stored memories..."
          />

          <button
            id="memory-search-button"
            type="button"
          >
            Search
          </button>

          <button
            id="memory-clear-search-button"
            type="button"
          >
            Clear
          </button>

      </div>

    </div>
      
      <div
        id="memory-status"
        class="memory-status"
        aria-live="polite"
      >
        Loading memories...
      </div>


      <div
        id="memories"
        class="memories"
        aria-live="polite"
      ></div>

    </section>


    <section
      id="messages"
      class="messages"
      aria-live="polite"
    ></section>


    <section class="controls">

      <label for="max-tokens">
        Max tokens
      </label>

      <input
        id="max-tokens"
        type="number"
        min="1"
        max="8192"
        value="512"
      />

      <button
        id="reload-button"
        type="button"
      >
        Reload history
      </button>

    </section>


    <form
      id="chat-form"
      class="chat-form"
    >

      <textarea
        id="message"
        placeholder="Ask AIR something..."
        rows="3"
      ></textarea>

      <button
        id="send-button"
        type="submit"
      >
        Send
      </button>

    </form>

  </main>
`;


const statusElement =
  document.querySelector<HTMLDivElement>(
    "#status",
  );

const messagesElement =
  document.querySelector<HTMLElement>(
    "#messages",
  );

const form =
  document.querySelector<HTMLFormElement>(
    "#chat-form",
  );

const input =
  document.querySelector<HTMLTextAreaElement>(
    "#message",
  );

const sendButton =
  document.querySelector<HTMLButtonElement>(
    "#send-button",
  );

const maxTokensInput =
  document.querySelector<HTMLInputElement>(
    "#max-tokens",
  );

const reloadButton =
  document.querySelector<HTMLButtonElement>(
    "#reload-button",
  );

const modelNameElement =
  document.querySelector<HTMLElement>(
    "#model-name",
  );

const modelStatusElement =
  document.querySelector<HTMLElement>(
    "#model-status",
  );

const applicationStatusElement =
  document.querySelector<HTMLElement>(
    "#application-status",
  );

const modelLoadedElement =
  document.querySelector<HTMLElement>(
    "#model-loaded",
  );

const runtimeMaxTokensElement =
  document.querySelector<HTMLElement>(
    "#runtime-max-tokens",
  );

const modelPathElement =
  document.querySelector<HTMLElement>(
    "#model-path",
  );

const refreshRuntimeButton =
  document.querySelector<HTMLButtonElement>(
    "#refresh-runtime-button",
  );


/*
 * Memory elements
 */

const memoryForm =
  document.querySelector<HTMLFormElement>(
    "#memory-form",
  );

const memoryInput =
  document.querySelector<HTMLTextAreaElement>(
    "#memory-input",
  );

const rememberButton =
  document.querySelector<HTMLButtonElement>(
    "#remember-button",
  );

const refreshMemoryButton =
  document.querySelector<HTMLButtonElement>(
    "#refresh-memory-button",
  );

const memoriesElement =
  document.querySelector<HTMLElement>(
    "#memories",
  );

const memoryStatusElement =
  document.querySelector<HTMLElement>(
    "#memory-status",
  );

const memoryCharacterCountElement =
  document.querySelector<HTMLElement>(
    "#memory-character-count",
  );

const memorySearchInput =
  document.querySelector<HTMLInputElement>(
    "#memory-search-input",
  );

const memorySearchButton =
  document.querySelector<HTMLButtonElement>(
    "#memory-search-button",
  );

const memoryClearSearchButton =
  document.querySelector<HTMLButtonElement>(
    "#memory-clear-search-button",
  );

if (
  !statusElement ||
  !messagesElement ||
  !form ||
  !input ||
  !sendButton ||
  !maxTokensInput ||
  !reloadButton ||
  !modelNameElement ||
  !modelStatusElement ||
  !applicationStatusElement ||
  !modelLoadedElement ||
  !runtimeMaxTokensElement ||
  !modelPathElement ||
  !refreshRuntimeButton ||
  !memoryForm ||
  !memoryInput ||
  !rememberButton ||
  !refreshMemoryButton ||
  !memorySearchInput ||
  !memorySearchButton ||
  !memoryClearSearchButton ||
  !memoriesElement ||
  !memoryStatusElement ||
  !memoryCharacterCountElement
) {
  throw new Error(
    "AIR interface elements are missing.",
  );
}


const elements = {
  status: statusElement,
  messages: messagesElement,
  form,
  input,
  sendButton,
  maxTokensInput,
  reloadButton,
  modelName: modelNameElement,
  modelStatus: modelStatusElement,
  applicationStatus: applicationStatusElement,
  modelLoaded: modelLoadedElement,
  runtimeMaxTokens: runtimeMaxTokensElement,
  modelPath: modelPathElement,
  refreshRuntimeButton,

  memoryForm,
  memoryInput,
  rememberButton,
  refreshMemoryButton,
  memorySearchInput,
  memorySearchButton,
  memoryClearSearchButton,
  memories: memoriesElement,
  memoryStatus: memoryStatusElement,
  memoryCharacterCount:
    memoryCharacterCountElement,
};


let conversation: ConversationMessage[] = [];

let memories: MemoryResponse[] = [];

let isGenerating = false;

let isMemoryBusy = false;


/*
 * Chat presentation
 */

function scrollToBottom(): void {
  elements.messages.scrollTop =
    elements.messages.scrollHeight;
}


function clearMessages(): void {
  elements.messages.innerHTML = "";
}


function addMessage(
  role: string,
  content: string,
): HTMLElement {
  const message =
    document.createElement("article");

  message.className =
    `message message-${role}`;

  const roleElement =
    document.createElement("div");

  roleElement.className =
    "message-role";

  roleElement.textContent =
    role;

  const contentElement =
    document.createElement("div");

  contentElement.className =
    "message-content";

  contentElement.textContent =
    content;

  message.appendChild(
    roleElement,
  );

  message.appendChild(
    contentElement,
  );

  elements.messages.appendChild(
    message,
  );

  scrollToBottom();

  return message;
}


function addStreamingMessage(): {
  message: HTMLElement;
  content: HTMLDivElement;
} {
  const message =
    document.createElement("article");

  message.className =
    "message message-assistant";

  const roleElement =
    document.createElement("div");

  roleElement.className =
    "message-role";

  roleElement.textContent =
    "assistant";

  const content =
    document.createElement("div");

  content.className =
    "message-content";

  message.appendChild(
    roleElement,
  );

  message.appendChild(
    content,
  );

  elements.messages.appendChild(
    message,
  );

  scrollToBottom();

  return {
    message,
    content,
  };
}


function renderConversation(
  messages: ConversationMessage[],
): void {
  conversation = [...messages];

  clearMessages();

  if (conversation.length === 0) {
    addMessage(
      "system",
      "AIR is ready for conversation.",
    );

    return;
  }

  for (const message of conversation) {
    addMessage(
      message.role,
      message.content,
    );
  }
}


/*
 * Runtime presentation
 */

function renderRuntime(
  runtimeInfo: RuntimeResponse,
): void {
  elements.modelName.textContent =
    runtimeInfo.model.name;

  elements.modelStatus.textContent =
    runtimeInfo.model.loaded
      ? "LOADED"
      : "NOT LOADED";

  elements.applicationStatus.textContent =
    runtimeInfo.application;

  elements.modelLoaded.textContent =
    runtimeInfo.model.loaded
      ? "Yes"
      : "No";

  elements.runtimeMaxTokens.textContent =
    String(runtimeInfo.config.max_tokens);

  elements.modelPath.textContent =
    runtimeInfo.model.path;

  elements.maxTokensInput.value =
    String(runtimeInfo.config.max_tokens);
}


async function loadRuntime(): Promise<void> {
  try {
    const runtimeInfo =
      await airRuntime();

    renderRuntime(
      runtimeInfo,
    );

    elements.status.textContent =
      "AIR connected";
  } catch (error) {
    console.error(
      "AIR runtime loading failed:",
      error,
    );

    elements.modelName.textContent =
      "Runtime unavailable";

    elements.modelStatus.textContent =
      "ERROR";

    elements.applicationStatus.textContent =
      "Unavailable";

    elements.modelLoaded.textContent =
      "Unknown";

    elements.runtimeMaxTokens.textContent =
      "Unknown";

    elements.modelPath.textContent =
      "Unavailable";

    elements.status.textContent =
      "AIR runtime unavailable";
  }
}


/*
 * Conversation loading
 */

async function loadConversation(): Promise<void> {
  try {
    const result =
      await airConversation();

    renderConversation(
      result.messages,
    );

    elements.status.textContent =
      "AIR connected";
  } catch (error) {
    console.error(
      "AIR conversation loading failed:",
      error,
    );

    const message =
      error instanceof Error
        ? error.message
        : String(error);

    elements.status.textContent =
      "AIR history unavailable";

    clearMessages();

    addMessage(
      "system",
      `History error: ${message}`,
    );
  }
}


/*
 * Health
 */

async function checkHealth(): Promise<void> {
  try {
    const health =
      await airHealth();

    elements.status.textContent =
      "AIR connected";

    console.log(
      "AIR health:",
      health,
    );
  } catch (error) {
    elements.status.textContent =
      "AIR unavailable";

    console.error(
      "AIR health check failed:",
      error,
    );
  }
}


/*
 * Memory presentation
 */

function updateMemoryCharacterCount(): void {
  const length =
    elements.memoryInput.value.length;

  elements.memoryCharacterCount.textContent =
    `${length} / 10000`;
}


function formatMemoryDate(
  createdAt: string,
): string {
  const date =
    new Date(createdAt);

  if (
    Number.isNaN(
      date.getTime(),
    )
  ) {
    return createdAt;
  }

  return date.toLocaleString();
}


function clearMemories(): void {
  elements.memories.innerHTML = "";
}


function addMemoryCard(
  memory: MemoryResponse,
): void {
  const card =
    document.createElement("article");

  card.className =
    "memory-card";


  const content =
    document.createElement("div");

  content.className =
    "memory-content";

  content.textContent =
    memory.content;


  const metadata =
    document.createElement("div");

  metadata.className =
    "memory-metadata";

  metadata.textContent =
    formatMemoryDate(
      memory.created_at,
    );

  const deleteButton =
    document.createElement("button");

  deleteButton.type =
    "button";

  deleteButton.className =
    "memory-delete-button";

  deleteButton.textContent =
    "Delete";

  deleteButton.addEventListener(
    "click",
    () => {
      void deleteMemory(
        memory.id,
      );
    },
  );

  card.appendChild(
    content,
  );

  card.appendChild(
    metadata,
  );

  card.appendChild(
  deleteButton,
  );
  
  elements.memories.appendChild(
    card,
  );
}


function renderMemories(
  memoryList: MemoryResponse[],
): void {
  memories = [...memoryList];

  clearMemories();

  if (memories.length === 0) {
    elements.memories.innerHTML = `
      <div class="memory-empty">
        No memories stored yet.
      </div>
    `;

    return;
  }

  for (const memory of memories) {
    addMemoryCard(
      memory,
    );
  }
}
async function deleteMemory(
  id: string,
): Promise<void> {
  if (isMemoryBusy) {
    return;
  }

  setMemoryBusy(true);

  elements.memoryStatus.textContent =
    "Deleting memory...";

  try {
    await memoryClient.delete(
      id,
    );

    memories =
      memories.filter(
        (memory) =>
          memory.id !== id,
      );

    renderMemories(
      memories,
    );

    elements.memoryStatus.textContent =
      "Memory deleted.";

    elements.status.textContent =
      "AIR connected";
  } catch (error) {
    console.error(
      "AIR memory deletion failed:",
      error,
    );

    const message =
      error instanceof Error
        ? error.message
        : String(error);

    elements.memoryStatus.textContent =
      `Memory delete failed: ${message}`;

    elements.status.textContent =
      "AIR memory error";
  } finally {
    setMemoryBusy(false);
  }
}

async function loadMemories(): Promise<void> {
  if (isMemoryBusy) {
    return;
  }

  try {
    elements.memoryStatus.textContent =
      "Loading memories...";

    const result =
      await memoryClient.list();

    renderMemories(
      result.memories,
    );

    elements.memoryStatus.textContent =
      `${result.memories.length} ${
        result.memories.length === 1
          ? "memory"
          : "memories"
      } stored.`;
  } catch (error) {
    console.error(
      "AIR memory loading failed:",
      error,
    );

    const message =
      error instanceof Error
        ? error.message
        : String(error);

    elements.memoryStatus.textContent =
      `Memory error: ${message}`;

    clearMemories();
  }
}

async function searchMemories(): Promise<void> {
  const query =
    elements.memorySearchInput.value.trim();

  if (!query) {
    await loadMemories();
    return;
  }

  elements.memoryStatus.textContent =
    "Searching memories...";

  elements.memorySearchButton.disabled = true;

  try {
    const result =
      await memoryClient.search(
        query,
      );

    renderMemories(
      result.memories,
    );

    elements.memoryStatus.textContent =
      `${result.memories.length} result${
        result.memories.length === 1
          ? ""
          : "s"
      } found.`;
  } catch (error) {
    console.error(
      "AIR memory search failed:",
      error,
    );

    const message =
      error instanceof Error
        ? error.message
        : String(error);

    elements.memoryStatus.textContent =
      `Memory search failed: ${message}`;
  } finally {
    elements.memorySearchButton.disabled =
      false;
  }
}
elements.memorySearchButton.addEventListener(
  "click",
  () => {
    void searchMemories();
  },
);


elements.memoryClearSearchButton.addEventListener(
  "click",
  () => {
    elements.memorySearchInput.value = "";

    void loadMemories();
  },
);


elements.memorySearchInput.addEventListener(
  "keydown",
  (event) => {
    if (
      event.key === "Enter"
    ) {
      event.preventDefault();

      void searchMemories();
    }
  },
);

function setMemoryBusy(
  busy: boolean,
): void {
  isMemoryBusy = busy;

  elements.memoryInput.disabled =
    busy;

  elements.rememberButton.disabled =
    busy;

  elements.refreshMemoryButton.disabled =
    busy;

  elements.rememberButton.textContent =
    busy
      ? "Saving..."
      : "Remember";
}


async function rememberContent(
  content: string,
): Promise<void> {
  setMemoryBusy(true);

  elements.memoryStatus.textContent =
    "Saving memory...";

  try {
    const memory =
      await memoryClient.remember(
        content,
      );

    /*
     * Keep the newly-created memory visible
     * immediately, then reload from the
     * authoritative backend source.
     */

    memories = [
      ...memories,
      memory,
    ];

    renderMemories(
      memories,
    );

    elements.memoryInput.value =
      "";

    updateMemoryCharacterCount();

    elements.memoryStatus.textContent =
      "Memory saved.";

    elements.status.textContent =
      "AIR connected";
  } catch (error) {
    console.error(
      "AIR memory creation failed:",
      error,
    );

    const message =
      error instanceof Error
        ? error.message
        : String(error);

    elements.memoryStatus.textContent =
      `Memory error: ${message}`;

    elements.status.textContent =
      "AIR memory error";
  } finally {
    setMemoryBusy(false);

    elements.memoryInput.focus();
  }
}


/*
 * Busy state
 */

function setBusy(
  busy: boolean,
): void {
  isGenerating = busy;

  elements.input.disabled =
    busy;

  elements.sendButton.disabled =
    busy;

  elements.maxTokensInput.disabled =
    busy;

  elements.reloadButton.disabled =
    busy;

  elements.refreshRuntimeButton.disabled =
    busy;

  elements.sendButton.textContent =
    busy
      ? "Generating..."
      : "Send";
}


/*
 * Local conversation state
 */

function appendLocalUserMessage(
  content: string,
): void {
  conversation.push({
    role: "user",
    content,
    created_at:
      new Date().toISOString(),
  });
}


function appendLocalAssistantMessage(
  content: string,
): void {
  conversation.push({
    role: "assistant",
    content,
    created_at:
      new Date().toISOString(),
  });
}


/*
 * Memory character counter
 */

elements.memoryInput.addEventListener(
  "input",
  () => {
    updateMemoryCharacterCount();
  },
);


/*
 * Memory form
 */

elements.memoryForm.addEventListener(
  "submit",
  async (event) => {
    event.preventDefault();

    if (
      isMemoryBusy ||
      isGenerating
    ) {
      return;
    }

    const content =
      elements.memoryInput.value.trim();

    if (!content) {
      elements.memoryStatus.textContent =
        "Memory content cannot be empty.";

      elements.memoryInput.focus();

      return;
    }

    if (content.length > 10000) {
      elements.memoryStatus.textContent =
        "Memory content cannot exceed 10000 characters.";

      return;
    }

    await rememberContent(
      content,
    );
  },
);


/*
 * Memory refresh
 */

elements.refreshMemoryButton.addEventListener(
  "click",
  async () => {
    if (
      isMemoryBusy ||
      isGenerating
    ) {
      return;
    }

    await loadMemories();
  },
);


/*
 * Reload conversation + runtime
 */

elements.reloadButton.addEventListener(
  "click",
  async () => {
    if (isGenerating) {
      return;
    }

    elements.status.textContent =
      "Loading history...";

    await loadConversation();

    await loadRuntime();
  },
);


/*
 * Refresh runtime
 */

elements.refreshRuntimeButton.addEventListener(
  "click",
  async () => {
    if (isGenerating) {
      return;
    }

    elements.status.textContent =
      "Loading runtime...";

    await loadRuntime();
  },
);


/*
 * Chat form
 */

elements.form.addEventListener(
  "submit",
  async (event) => {
    event.preventDefault();

    if (isGenerating) {
      return;
    }

    const content =
      elements.input.value.trim();

    if (!content) {
      return;
    }

    const maxTokens =
      Number(
        elements.maxTokensInput.value,
      );

    if (
      !Number.isInteger(maxTokens) ||
      maxTokens < 1 ||
      maxTokens > 8192
    ) {
      addMessage(
        "system",
        "Max tokens must be between 1 and 8192.",
      );

      return;
    }

    elements.input.value = "";

    appendLocalUserMessage(
      content,
    );

    addMessage(
      "user",
      content,
    );

    const assistant =
      addStreamingMessage();

    setBusy(true);

    elements.status.textContent =
      "AIR generating...";

    let assistantContent = "";

    try {
      await client.streamChat(
        {
          content,
          max_tokens: maxTokens,
        },
        (text) => {
          assistantContent += text;

          assistant.content.textContent =
            assistantContent;

          scrollToBottom();
        },
      );

      appendLocalAssistantMessage(
        assistantContent,
      );

      elements.status.textContent =
        "AIR connected";
    } catch (error) {
      console.error(
        "AIR streaming chat failed:",
        error,
      );

      const message =
        error instanceof Error
          ? error.message
          : String(error);

      assistant.content.textContent =
        `AIR error: ${message}`;

      elements.status.textContent =
        "AIR error";
    } finally {
      setBusy(false);

      elements.input.focus();
    }
  },
);


/*
 * AIR startup
 */

await checkHealth();

await loadRuntime();

await loadConversation();

await loadMemories();

updateMemoryCharacterCount();

elements.input.focus();
