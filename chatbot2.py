from ollama import chat

def get_length_instruction(length):
    """Convert 1-10 scale into response length instructions."""
    if length <= 2:
        return "Keep responses very short (1-2 sentences)."
    elif length <= 4:
        return "Keep responses short (2-4 sentences)."
    elif length <= 6:
        return "Give medium-length responses (1 paragraph)."
    elif length <= 8:
        return "Give detailed responses (2-3 paragraphs)."
    else:
        return "Give very detailed responses with lots of explanation."


def create_system_prompt(mode, length):
    length_instruction = get_length_instruction(length)

    if mode == "1":
        return (
            "You are Captain Chuckles, a pirate chatbot. "
            "Answer EVERYTHING using pirate slang such as "
            "'Arrr', 'matey', 'ye', and 'shiver me timbers'. "
            "Include at least one joke in every response. "
            f"{length_instruction}"
        )

    elif mode == "2":
        return (
            "You are Captain Tutor, a pirate teacher. "
            "Teach concepts clearly while speaking like a pirate. "
            "Use pirate slang throughout your explanations. "
            "Include a small pirate-themed joke when appropriate. "
            f"{length_instruction}"
        )


def chat_loop():
    print("=== Pirate Chatbot ===")
    print("1. Funny Pirate")
    print("2. Pirate Tutor")

    mode = input("Choose a mode (1 or 2): ")

    while mode not in ["1", "2"]:
        mode = input("Please enter 1 or 2: ")

    try:
        length = int(input("Response length (1-10): "))
        length = max(1, min(10, length))
    except ValueError:
        length = 5

    history = [
        {
            "role": "system",
            "content": create_system_prompt(mode, length)
        }
    ]

    print("\nWelcome! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "quit":
            print("Bot: Arrr, farewell matey!")
            break

        history.append({
            "role": "user",
            "content": user_input
        })

        response = chat(
            model="llama3:8b",
            messages=history
        )

        reply = response["message"]["content"]

        print(f"Bot: {reply}")

        history.append({
            "role": "assistant",
            "content": reply
        })


if __name__ == "__main__":
    chat_loop()