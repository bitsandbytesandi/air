from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    content: str = Field(
        min_length=1,
        max_length=20_000,
    )
    max_tokens: int | None = Field(
        default=None,
        ge=1,
        le=8192,
    )


class ChatResponse(BaseModel):
    content: str


class ConversationMessage(BaseModel):
    role: str
    content: str
    created_at: str


class ConversationResponse(BaseModel):
    messages: list[ConversationMessage]


class HealthResponse(BaseModel):
    status: str
    application: str


class ModelInfoResponse(BaseModel):
    name: str
    path: str
    loaded: bool


class RuntimeConfigResponse(BaseModel):
    max_tokens: int


class RuntimeResponse(BaseModel):
    status: str
    application: str
    model: ModelInfoResponse
    config: RuntimeConfigResponse


class StreamChunk(BaseModel):
    text: str


class StreamDone(BaseModel):
    done: bool
