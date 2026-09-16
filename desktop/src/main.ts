import "./styles.css";

import {
  airConversation,
  airHealth,
  airRuntime,
  type ConversationMessage,
  type RuntimeResponse,
} from "./api/ipc";

import {
  AirClient,
} from "./api/client";

const client = new AirClient();

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
  !refreshRuntimeButton
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
};

let conversation: ConversationMessage[] = [];

let isGenerating = false;

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
  }
      finally {
      setBusy(false);

      elements.input.focus();
    }
  },
);

await checkHealth();

await loadRuntime();

await loadConversation();

elements.input.focus();
