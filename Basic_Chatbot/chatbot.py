import datetime

def get_response(user_input):
    """Returns a predefined response based on the user's input."""
    user_input = user_input.lower().strip()
    
    if not user_input:
        return "Please say something! Type 'help' if you're not sure what to say."
        
    if user_input in ["hello", "hi", "hey", "greetings"]:
        return "Hi there! Nice to meet you. How can I help you today?"
        
    elif user_input in ["good morning", "good afternoon", "good evening"]:
        return f"{user_input.capitalize()} to you too!"
        
    elif "how are you" in user_input:
        return "I'm just a bunch of Python code, but I'm doing great! How are you?"
        
    elif "what is your name" in user_input or "who are you" in user_input:
        return "My name is PyBot. I am a simple rule-based chatbot."
        
    elif "time" in user_input:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."
        
    elif "date" in user_input:
        now = datetime.datetime.now()
        return f"Today's date is {now.strftime('%B %d, %Y')}."
        
    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
        
    elif "help" in user_input:
        return display_help()
        
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what I can answer."

def display_help():
    """Returns a string containing the supported commands."""
    help_text = (
        "I am a simple rule-based bot. Here are some things you can ask me:\n"
        "  - 'hello' or 'hi'\n"
        "  - 'how are you?'\n"
        "  - 'what is your name?'\n"
        "  - 'tell me a joke'\n"
        "  - 'what is the time?'\n"
        "  - 'what is the date?'\n"
        "  - 'help'\n"
        "  - 'bye' or 'exit' (to end the chat)"
    )
    return help_text

def chat():
    """Main loop for continuous conversation."""
    print("========================================")
    print("          PYTHON BASIC CHATBOT          ")
    print("========================================")
    print("\nBot: Hello! I am your Python chatbot.")
    print("Bot: Type 'help' to see what I can do.")
    print("Bot: Type 'bye', 'exit', or 'quit' to exit.\n")
    
    while True:
        try:
            user_input = input("You: ")
            
            clean_input = user_input.lower().strip()
            if clean_input in ["bye", "exit", "quit", "goodbye"]:
                print("Bot: Goodbye! Have a great day!")
                break
                
            response = get_response(user_input)
            print(f"Bot: {response}\n")
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"Bot: Oops! Something went wrong: {e}")

def main():
    """Main entry point of the script."""
    chat()

if __name__ == "__main__":
    main()
