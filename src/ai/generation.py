from mlx_lm import generate

def generate_response(model, tokenizer, prompt, max_tokens=1024):
    response = generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=max_tokens,
    )

    return response.strip()
