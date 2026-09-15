# Basic Rule-Based Chatbot

## Description
A simple, interactive, rule-based chatbot built entirely in Python. The chatbot communicates through the terminal, recognizing predefined user messages and responding with appropriate replies.

## Objective
To build a functional command-line chatbot that demonstrates the use of continuous loops, user input handling, string normalization, and control flow (if-elif-else conditions) without relying on external APIs or complex machine learning models.

## Features
- **Continuous Conversation**: Uses a `while` loop to maintain a continuous chat session until the user decides to exit.
- **Rule-Based Responses**: Recognizes common phrases like "hello", "how are you", "joke", "time", and "date".
- **Dynamic Content**: Uses Python's `datetime` module to fetch and return the real-time date and time when asked.
- **Case-Insensitive**: Normalizes all user input to lowercase so "Hello", "HELLO", and "hello" are treated equally.
- **Graceful Error Handling**: Manages empty inputs, unknown phrases, and keyboard interruptions (Ctrl+C) smoothly without crashing.

## Technologies Used
- **Python 3**: Core language.
- **`datetime` module**: Standard library module used to calculate the current time and date.

## Python Concepts Demonstrated
- **String Manipulation**: `.lower()`, `.strip()`, and keyword checking using the `in` operator.
- **Control Flow**: Extensive use of `if-elif-else` branches to act as the "brain" or rule engine.
- **Functions**: Encapsulating logic into `get_response()`, `display_help()`, and `chat()` for clean, readable code.
- **Infinite Loops & Break Statements**: Using `while True` to keep the bot alive until `break` is triggered by an exit command.

## How the Chatbot Works
1. The program starts the `chat()` function, printing a welcome message and entering a `while True` loop.
2. It waits for the user to type something using `input()`.
3. It checks if the user typed an exit command ("bye", "exit"). If so, it breaks the loop and closes.
4. If not, it passes the input to `get_response()`.
5. `get_response()` strips extra spaces, converts the text to lowercase, and checks it against a series of `if/elif` rules.
6. The bot returns the predefined string matching the rule, or a fallback message if it doesn't understand.
7. The loop repeats.

## Project Structure
```text
Basic_Chatbot/
│
├── chatbot.py               # Main script containing chatbot logic
├── README.md                # Project documentation
└── requirements.txt         # Dependency information
```

## Installation & Execution
This project uses only standard Python libraries. No extra installation is required.
1. Navigate to the project directory in your terminal.
2. Run the script:
   ```bash
   python chatbot.py
   ```

## Example Conversation
```text
========================================
          PYTHON BASIC CHATBOT          
========================================

Bot: Hello! I am your Python chatbot.
Bot: Type 'help' to see what I can do.
Bot: Type 'bye', 'exit', or 'quit' to exit.

You: hello
Bot: Hi there! Nice to meet you. How can I help you today?

You: What is your name?
Bot: My name is PyBot. I am a simple rule-based chatbot.

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: what is the time
Bot: The current time is 01:30 PM.

You: explain quantum physics
Bot: Sorry, I don't understand that yet. Type 'help' to see what I can answer.

You: bye
Bot: Goodbye! Have a great day!
```

## ⚠️ Important Limitations
This chatbot is strictly **rule-based**. Therefore:
- It **cannot** understand arbitrary, complex, or conversational questions outside its programmed rules.
- It **does not** learn automatically from user interactions.
- Responses are 100% **predefined** by the developer.
- It is **not** a Generative AI system (like ChatGPT). It does not use NLP (Natural Language Processing) or Machine Learning.

## Future Enhancements
- Expand the dictionary of rules to handle more conversational topics.
- Allow the bot to read rules from an external JSON or CSV file instead of hardcoding them into `if` statements.
- Add simple math calculation capabilities (e.g., "Calculate 5 + 5").

## Author
Developed as part of the **CodeAlpha Python Programming Internship**.
