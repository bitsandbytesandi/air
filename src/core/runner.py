from core.bootstrap import create_application

def run() -> None:
    application = create_application()

    application.start()

    print("AIR is ready. Type 'exit' to quit.\n")

    while True:
        content = input("You: ")

        if content.lower() == "exit":
            print("Goodbye.")
            break

        response = application.chat(content)

        print(f"AIR: {response.content}\n")
