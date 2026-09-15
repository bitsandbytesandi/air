from collections.abc import Iterator

from mlx_lm import generate, stream_generate

from core.errors import GenerationError


DEFAULT_MAX_TOKENS = 1024


def _resolve_max_tokens(max_tokens: int | None) -> int:
    if max_tokens is None:
        return DEFAULT_MAX_TOKENS

    if max_tokens < 1:
        raise ValueError(
            "max_tokens must be greater than zero."
        )

    return max_tokens


def generate_response(
    model,
    tokenizer,
    prompt,
    max_tokens=None,
) -> str:
    resolved_max_tokens = _resolve_max_tokens(
        max_tokens
    )

    try:
        response = generate(
            model,
            tokenizer,
            prompt=prompt,
            max_tokens=resolved_max_tokens,
        )
    except Exception as exc:
        raise GenerationError(
            "AI generation failed."
        ) from exc

    return response.strip()


def stream_response(
    model,
    tokenizer,
    prompt,
    max_tokens=None,
) -> Iterator[str]:
    resolved_max_tokens = _resolve_max_tokens(
        max_tokens
    )

    try:
        for response in stream_generate(
            model,
            tokenizer,
            prompt=prompt,
            max_tokens=resolved_max_tokens,
        ):
            if response.text:
                yield response.text

    except Exception as exc:
        raise GenerationError(
            "AI streaming generation failed."
        ) from exc
