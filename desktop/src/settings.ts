import {
  airSettings,
  airUpdateSettings,
} from "./api/ipc";

export function createSettingsPanel(): HTMLElement {
  const panel = document.createElement("section");

  panel.innerHTML = `
    <div class="settings-panel">
      <h2>Settings</h2>

      <label for="settings-max-tokens">
        Max tokens
      </label>

      <input
        id="settings-max-tokens"
        type="number"
        min="1"
        max="8192"
        value="512"
      />

      <button id="settings-save">
        Save settings
      </button>

      <span id="settings-status"></span>
    </div>
  `;

  const input =
    panel.querySelector<HTMLInputElement>(
      "#settings-max-tokens"
    );

  const saveButton =
    panel.querySelector<HTMLButtonElement>(
      "#settings-save"
    );

  const status =
    panel.querySelector<HTMLSpanElement>(
      "#settings-status"
    );

  if (!input || !saveButton || !status) {
    throw new Error(
      "Settings panel elements could not be created."
    );
  }

  void airSettings()
    .then((settings) => {
      input.value = String(settings.max_tokens);
    })
    .catch(() => {
      status.textContent =
        "Could not load settings.";
    });

  saveButton.addEventListener("click", async () => {
    const maxTokens = Number(input.value);

    if (
      !Number.isInteger(maxTokens) ||
      maxTokens < 1 ||
      maxTokens > 8192
    ) {
      status.textContent =
        "Max tokens must be between 1 and 8192.";
      return;
    }

    try {
      await airUpdateSettings(maxTokens);

      status.textContent =
        "Settings saved.";
    } catch {
      status.textContent =
        "Could not save settings.";
    }
  });

  return panel;
}
