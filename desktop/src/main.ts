import "./styles.css";

import {
  airConversation,
  airHealth,
  airRuntime,
  type ConversationMessage,
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
        max="4096"
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

if (
  !statusElement ||
  !messagesElement ||
  !form ||
  !input ||
  !sendButton ||
  !maxTokensInput ||
  !reloadButton
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

    elements.status.textContent =
      "AIR history unavailable";

    clearMessages();

    addMessage(
      "system",
      "Conversation history could not be loaded.",
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

  elements.input.disabled = busy;

  elements.sendButton.disabled =
    busy;

  elements.maxTokensInput.disabled =
    busy;

  elements.reloadButton.disabled =
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
      maxTokens > 4096
    ) {
      addMessage(
        "system",
        "Max tokens must be between 1 and 4096.",
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

      assistant.content.textContent =
        "AIR could not generate a response.";

      elements.status.textContent =
        "AIR error";
    } finally {
      setBusy(false);

      elements.input.focus();
    }
  },
);

await checkHealth();

await loadConversation();

elements.input.focus();
