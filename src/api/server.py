import json
import os
import secrets
from contextlib import asynccontextmanager
from collections.abc import Iterator

from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.responses import StreamingResponse

from api.schemas import (
    ChatRequest,
    ChatResponse,
    ConversationResponse,
    HealthResponse,
)

from core.application import ApplicationService
from core.bootstrap import create_application


application: ApplicationService | None = None


def require_api_token(
    authorization: str | None = Header(default=None),
) -> None:
    expected_token = os.getenv("AIR_API_TOKEN")

    if not expected_token:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AIR_API_TOKEN is not configured.",
        )

    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header required.",
        )

    scheme, _, token = authorization.partition(" ")

    if scheme.lower() != "bearer" or not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required.",
        )

    if not secrets.compare_digest(
        token,
        expected_token,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token.",
        )


def get_application() -> ApplicationService:
    if application is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AIR application is not ready.",
        )

    return application


@asynccontextmanager
async def lifespan(app: FastAPI):
    global application

    application = create_application()
    application.start()

    try:
        yield
    finally:
        application.shutdown()
        application = None


app = FastAPI(
    title="AIR Local API",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get(
    "/v1/health",
    response_model=HealthResponse,
)
def health(
    _: None = Depends(require_api_token),
    service: ApplicationService = Depends(get_application),
):
    return HealthResponse(
        status="ok",
        application=service.state.value,
    )


@app.get(
    "/v1/conversation",
    response_model=ConversationResponse,
)
def conversation(
    _: None = Depends(require_api_token),
    service: ApplicationService = Depends(get_application),
):
    return ConversationResponse(
        messages=service.get_conversation()
    )


@app.post(
    "/v1/chat",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
    _: None = Depends(require_api_token),
    service: ApplicationService = Depends(get_application),
):
    result = service.chat(
        content=request.content,
        max_tokens=request.max_tokens,
    )

    return ChatResponse(
        content=result.content
    )


@app.post(
    "/v1/chat/stream",
)
def chat_stream(
    request: ChatRequest,
    _: None = Depends(require_api_token),
    service: ApplicationService = Depends(get_application),
):
    def event_stream() -> Iterator[str]:
        for chunk in service.stream_chat(
            content=request.content,
            max_tokens=request.max_tokens,
        ):
            payload = json.dumps(
                {"text": chunk},
                ensure_ascii=False,
            )

            yield f"data: {payload}\n\n"

        yield 'data: {"done": true}\n\n'

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
