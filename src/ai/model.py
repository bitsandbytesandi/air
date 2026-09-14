from pathlib import Path

from mlx_lm import load


MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "models"
    / "Qwen3.6-27B-MLX-6bit"
)

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found: {MODEL_PATH}"
        )

    model, tokenizer = load(str(MODEL_PATH))
    return model, tokenizer
