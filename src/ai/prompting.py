def build_prompt(tokenizer, question):
    messages = [
        {
            "role": "user",
            "content": question,
        }
    ]

    return tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True
    )

def build_conversation_prompt(tokenizer, messages):
    return tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=False,
    )
