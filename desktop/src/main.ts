import "./styles.css";

import { AirClient } from "./api/client";

const client = new AirClient();

const app = document.querySelector<HTMLDivElement>("#app");

if (!app) {
  throw new Error("AIR application root was not found.");
}

app.innerHTML = `
  <main class="air-shell">
    <header class="air-header">
      <div>
        <h1>AIR</h1>
        <p>Artificial Intelligence Runtime</p>
      </div>

      <div id="status" class="status">
        Checking AIR...
      </div>
    </header>

    <section id="messages" class="messages">
      <div class="empty-state">
        <h2>Welcome to AIR</h2>
        <p>
          Your local AI runtime is ready for conversation.
        </p>
      </div>
    </section>

    <form id="chat-form" class="chat-form">
      <textarea
        id="message"
        placeholder="Ask AIR something..."
        rows="3"
      ></textarea>

      <button type="submit">
        Send
      </button>
    </form>
  </main>
`;

const statusElement =
  document.querySelector<HTMLDivElement>("#status");

const messagesElement =
  document.querySelector<HTMLDivElement>("#messages");

const form =
  document.querySelector<HTMLFormElement>("#chat-form");

const input =
  document.querySelector<HTMLTextAreaElement>("#message");

if (
  !statusElement ||
  !messagesElement ||
  !form ||
  !input
) {
  throw new Error(
    "AIR interface elements are missing.",
  );
}

async function checkHealth(): Promise<void> {
  try {
    const health = await client.health();

    statusElement.textContent =
      "AIR connected";

    console.log(
      "AIR health:",
      health,
    );
  } catch (error) {
    statusElement.textContent =
      "AIR unavailable";

    console.error(
      "AIR health check failed:",
      error,
    );
  }
}

function addMessage(
  role: string,
  content: string,
): HTMLDivElement {
  const message =
    document.createElement("article");

  message.className =
    `message message-${role}`;

  message.innerHTML = `
    <div class="message-role">
      ${role}
    </div>

    <div class="message-content"></div>
  `;

  const contentElement =
    message.querySelector<HTMLDivElement>(
      ".message-content",
    );

  if (!contentElement) {
    throw new Error(
      "Message content element missing.",
    );
  }

  contentElement.textContent = content;

  messagesElement.appendChild(message);

  messagesElement.scrollTop =
    messagesElement.scrollHeight;

  return message;
}

form.addEventListener(
  "submit",
  async (event) => {
    event.preventDefault();

    const content =
      input.value.trim();

    if (!content) {
      return;
    }

    input.value = "";

    addMessage(
      "user",
      content,
    );

    try {
      const response =
        await client.chat({
          content,
          max_tokens: 512,
        });

      addMessage(
        "assistant",
        response.content,
      );
    } catch (error) {
      console.error(
        "AIR chat failed:",
        error,
      );

      addMessage(
        "system",
        "AIR could not generate a response.",
      );
    }
  },
);

await checkHealth();
