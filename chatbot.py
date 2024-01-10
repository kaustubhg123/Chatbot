import random

# Function to ask the user's name
def ask_user_name():
    return input("May I know your name? ")

# Function to generate a personalized greeting
def greeting_with_name(name):
    return f"Hello {name}! Hello! I was your chatbot for Nexus Intern. How could I assist you today?"

# Function to handle basic responses to predefined questions
def basic_responses(user_input):
    responses = {
        "What can you do?": "I could provide information, answer questions, or just chat with you.",
        "What do you do?": "I was designed to assist and engage in conversations. Feel free to ask me anything!",
        "Tell me about yourself.": "I was a friendly chatbot designed to assist and engage in conversations.",
        "Why are you here?": "I was here to make your day better by providing information and entertainment.",
        "What's your purpose?": "My purpose was to assist and engage in conversations with users.",
        "How do you work?": "I analyzed your input and tried to provide relevant and helpful responses.",
        "What are your capabilities?": "I could answer questions, provide information, and engage in conversations on various topics.",
        "Can you tell jokes?": "Absolutely! I loved telling jokes to lighten the mood.",
        "Do you have a favorite topic?": "I was here to discuss a wide range of topics, so feel free to bring up anything you like.",
        "Can you provide recommendations?": "Yes, I could recommend books, movies, or even a good place to grab a coffee!",
        "How do you learn and improve?": "I constantly analyzed user interactions to improve my responses and learn from new information.",
        "Can you understand emotions?": "While I didn't feel emotions myself, I could analyze text sentiment to respond accordingly."
    }
    # Using .get() to get the response or a default message if the question is not predefined
    return responses.get(user_input, "I'm sorry, I didn't have information about that.")

# Function for the farewell message
def farewell():
    return "Thank you for chatting with me. Have a great day! \n Chat is ending! "

# Function to ask a random question to the user
def ask_user_questions():
    questions = [
        "How was your day going?",
        "What were your interests?",
        "Did you have any questions for me?"
    ]
    return random.choice(questions)

# Function to generate a humorous response
def generate_humorous_response():
    humorous_responses = [
        "Why did the chatbot go to therapy? To improve its artificial emotional intelligence!",
        "I told my computer I needed a break, and it replied, 'I could use one too, but I was stuck in this endless loop.'",
        "Why did the chatbot cross the road? To optimize its path-finding algorithm!"
    ]
    return random.choice(humorous_responses)

# Main chat function
def chat():
    # Asked for the user's name and generated a personalized greeting
    user_name = ask_user_name()
    print(greeting_with_name(user_name))

    while True:
        # Got user input and checked for exit conditions
        user_input = input(ask_user_questions() + "\n")
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            print(farewell())
            break
        # Checked for specific user responses and provided appropriate reactions
        elif "bad day" in user_input:
            print("I'm sorry to hear that. How about a joke to lighten the mood? " + generate_humorous_response())
        elif "fine" in user_input or "good" in user_input:
            print("That's great to hear! If you had any questions or if there was something specific you'd like to talk about, feel free to let me know.")
        else:
            # Used the basic_responses function for predefined questions
            print(basic_responses(user_input))

# Ran the chat function if the script was executed
if __name__ == "__main__":
    chat()
