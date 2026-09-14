from core.context import ApplicationContext


fake_chat_service = object()
fake_model = object()
fake_tokenizer = object()


context = ApplicationContext(
    chat_service=fake_chat_service,
    model=fake_model,
    tokenizer=fake_tokenizer,
)


assert context.chat_service is fake_chat_service
assert context.model is fake_model
assert context.tokenizer is fake_tokenizer


print("Brick 33 - Application context: GREEN")
