from mlx_lm import generate

DEFAULT_MAX_TOKENS = 1024

def generate_response(
    model, 
    tokenizer, 
    prompt, 
    max_tokens=DEFAULT_MAX_TOKENS,
) -> str:
    response = generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=max_tokens,
    )

    return response.strip()
