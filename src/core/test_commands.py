from core.commands import ChatCommand


command = ChatCommand(
    content="Hello AIR",
)


assert command.content == "Hello AIR"
assert command.max_tokens == 1280


custom_command = ChatCommand(
    content="Explain Python",
    max_tokens=256,
)


assert custom_command.content == "Explain Python"
assert custom_command.max_tokens == 256


print("Brick 34 - Command boundary: GREEN")
