# Basic Chatbot

A simple rule-based command-line chatbot in Python.

## Features

- Responds to greetings, simple questions, and thanks
- Tells a randomly selected joke
- Shows supported phrases with the `help` command
- Ignores capitalization, extra whitespace, and surrounding punctuation
- Handles empty or unknown messages with a helpful reply
- Keeps chatting until you type `bye`, `quit`, or `exit`
- Handles Ctrl+C and end-of-file gracefully

## How to Run

1. Make sure you have Python 3 installed. No extra packages are needed.
2. From the project root, run:

   ```bash
   python Beginner/basic-chatbot/basic_chatbot.py
   ```

   Or, from this folder, run `python basic_chatbot.py`.

## Example

```text
Welcome to Basic Chatbot!
MiniBot: Type help for ideas, or bye to leave.
You: Hello!
MiniBot: Hello! It's nice to chat with you.
You: What is your name?
MiniBot: I'm MiniBot, a basic Python chatbot.
You: joke
MiniBot: Why did the computer get cold? It left its Windows open!
You: thanks
MiniBot: You're welcome!
You: bye
MiniBot: Goodbye! Thanks for chatting.
```

Jokes are random, so the response may differ each time. MiniBot matches
whole phrases using `if` statements; it does not use AI, access the internet,
or learn from conversations. For example, `hello` is recognized, but
`hello everyone` receives the fallback reply.

To add a new topic, add a phrase rule and reply in `get_response()`, then
include the new topic in the help message.

---

Project for learning purposes.
