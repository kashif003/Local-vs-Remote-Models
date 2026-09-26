import ollama

MODEL = "llama3.2"

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Always answer briefly and concisely, in a few sentences at most.",
    }
]

print("Chat with the model. Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model=MODEL,
        messages=messages,
    )

    reply = response["message"]["content"]
    print(f"Bot: {reply}\n")

    messages.append({"role": "assistant", "content": reply})