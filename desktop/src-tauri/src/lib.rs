use reqwest::Client;
use serde::{Deserialize, Serialize};

const AIR_API_URL: &str = "http://127.0.0.1:8000";
const AIR_API_TOKEN: &str = "air-local-development-token";

#[derive(Debug, Serialize, Deserialize)]
struct HealthResponse {
    status: String,
    application: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct ConversationMessage {
    role: String,
    content: String,
    created_at: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct ConversationResponse {
    messages: Vec<ConversationMessage>,
}

#[derive(Debug, Serialize)]
struct ChatRequest {
    content: String,
    max_tokens: Option<u32>,
}

#[derive(Debug, Serialize, Deserialize)]
struct ChatResponse {
    content: String,
}
#[derive(Debug, Serialize, Deserialize)]
struct ModelInfo {
    name: String,
    path: String,
    loaded: bool,
}

#[derive(Debug, Serialize, Deserialize)]
struct RuntimeConfig {
    max_tokens: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct RuntimeResponse {
    status: String,
    application: String,
    model: ModelInfo,
    config: RuntimeConfig,
}
#[tauri::command]
async fn air_runtime() -> Result<RuntimeResponse, String> {
    let client = air_client()?;

    let response = air_request(
        client.get(format!("{AIR_API_URL}/v1/runtime"))
    )
    .send()
    .await
    .map_err(|error| {
        format!("AIR runtime request failed: {error}")
    })?;

    if !response.status().is_success() {
        return Err(format!(
            "AIR runtime request failed with status: {}",
            response.status()
        ));
    }

    response
        .json::<RuntimeResponse>()
        .await
        .map_err(|error| {
            format!(
                "Failed to decode AIR runtime response: {error}"
            )
        })
}

fn air_client() -> Result<Client, String> {
    Client::builder()
        .build()
        .map_err(|error| {
            format!("Failed to create AIR HTTP client: {error}")
        })
}

fn air_request(
    request: reqwest::RequestBuilder,
) -> reqwest::RequestBuilder {
    request.bearer_auth(AIR_API_TOKEN)
}

#[tauri::command]
async fn air_health() -> Result<HealthResponse, String> {
    let client = air_client()?;

    let response = air_request(
        client.get(format!("{AIR_API_URL}/v1/health")),
    )
    .send()
    .await
    .map_err(|error| {
        format!("AIR health request failed: {error}")
    })?;

    if !response.status().is_success() {
        return Err(format!(
            "AIR health returned HTTP {}",
            response.status()
        ));
    }

    response
        .json::<HealthResponse>()
        .await
        .map_err(|error| {
            format!("Invalid AIR health response: {error}")
        })
}

#[tauri::command]
async fn air_conversation() -> Result<ConversationResponse, String> {
    let client = air_client()?;

    let response = air_request(
        client.get(format!("{AIR_API_URL}/v1/conversation")),
    )
    .send()
    .await
    .map_err(|error| {
        format!("AIR conversation request failed: {error}")
    })?;

    if !response.status().is_success() {
        return Err(format!(
            "AIR conversation returned HTTP {}",
            response.status()
        ));
    }

    response
        .json::<ConversationResponse>()
        .await
        .map_err(|error| {
            format!("Invalid AIR conversation response: {error}")
        })
}

#[tauri::command]
async fn air_chat(
    content: String,
    max_tokens: Option<u32>,
) -> Result<ChatResponse, String> {
    if content.trim().is_empty() {
        return Err(
            "AIR chat message cannot be empty.".to_string()
        );
    }

    let client = air_client()?;

    let request = ChatRequest {
        content,
        max_tokens,
    };

    let response = air_request(
        client
            .post(format!("{AIR_API_URL}/v1/chat"))
            .json(&request),
    )
    .send()
    .await
    .map_err(|error| {
        format!("AIR chat request failed: {error}")
    })?;

    if !response.status().is_success() {
        let status = response.status();

        let body = response
            .text()
            .await
            .unwrap_or_else(|_| {
                "Unable to read AIR error response."
                    .to_string()
            });

        return Err(format!(
            "AIR chat returned HTTP {status}: {body}"
        ));
    }

    response
        .json::<ChatResponse>()
        .await
        .map_err(|error| {
            format!("Invalid AIR chat response: {error}")
        })
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![
            air_health,
            air_conversation,
            air_chat,
            air_runtime
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
