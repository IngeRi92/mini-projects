"""A rule-based command-line chatbot with simple replies and random jokes."""

import random
import string


def normalize_message(message):
    """Prepare a message for matching against the chatbot's known phrases.

    Ignore capitalization, extra whitespace, and punctuation at the
    beginning or end of the message. Keep punctuation inside words.

    Args:
        message (str): The user's original message.

    Returns:
        str: The cleaned, lowercase message.
    """
    return " ".join(message.lower().strip(string.whitespace + string.punctuation).split())


def get_response(message):
    """Choose a reply for a message using a fixed set of phrase rules.

    Match the whole cleaned message, so a word inside an unrelated
    sentence does not accidentally trigger a reply. Unknown messages
    receive a suggestion to use the help command.

    Args:
        message (str): The user's message, which may include mixed case
            or surrounding punctuation and whitespace.

    Returns:
        str: The chatbot's reply.
    """
    message = normalize_message(message)

    if not message:
        return "Please type a message so we can chat."
    if message in ("help", "what can you do"):
        return (
            "Try: hello, how are you, what is your name, joke, or thanks. "
            "Type bye, quit, or exit to leave."
        )
    if message in ("hi", "hello", "hey"):
        return "Hello! It's nice to chat with you."
    if message in ("how are you", "how are you doing"):
        return "I'm ready to chat and share a joke! How are you?"
    if message in ("good", "fine", "i'm fine", "i am fine", "i'm good", "i am good"):
        return "Glad to hear that!"
    if message in ("what is your name", "what's your name", "who are you"):
        return "I'm MiniBot, a basic Python chatbot."
    if message in ("joke", "tell me a joke"):
        return random.choice(
            [
                "Why did the computer get cold? It left its Windows open!",
                "Why do Python programmers wear glasses? Because they can't C!",
                "What do you call a bear with no teeth? A gummy bear!",
            ]
        )
    if message in ("thanks", "thank you"):
        return "You're welcome!"
    if message in ("bye", "quit", "exit"):
        return "Goodbye! Thanks for chatting."
    return "I don't know how to answer that yet. Type help to see what I understand."


def main():
    """Run the chat loop until the user leaves.

    Display a reply after each message. The commands 'bye', 'quit', and
    'exit' end the conversation, ignoring case and surrounding punctuation.
    End-of-file or Ctrl+C also closes the chatbot with a goodbye message.

    Returns:
        None.
    """
    print("Welcome to Basic Chatbot!")
    print("MiniBot: Type help for ideas, or bye to leave.")

    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nMiniBot: Goodbye! Thanks for chatting.")
            break

        print(f"MiniBot: {get_response(message)}")
        if normalize_message(message) in ("bye", "quit", "exit"):
            break


if __name__ == "__main__":
    main()
