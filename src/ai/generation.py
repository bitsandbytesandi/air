from mlx_lm import generate
from core.errors import GenerationError

DEFAULT_MAX_TOKENS = 1024

def generate_response(
    model, 
    tokenizer, 
    prompt, 
    max_tokens=DEFAULT_MAX_TOKENS,
) -> str:
    try:
        response = generate(
            model,
            tokenizer,
            prompt=prompt,
            max_tokens=max_tokens,
        )
    except Exception as exc:
        raise GenerationError(
            "AI generation failed."
        ) from exc

    return response.strip()
