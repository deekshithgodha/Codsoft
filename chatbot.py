# Function to handle user input and provide responses
def chatbot_response(user_input):
    # Convert the user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Predefined responses based on specific keywords
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "good morning" in user_input:
        return "Good morning! How can I help you?"
    elif "good afternoon" in user_input:
        return "Good afternoon! How can I help you?"
    elif "good evening" in user_input:
        return "Good evening! How can I help you?"
    elif "what is your name?" in user_input:
        return "My name is NANI and I am a rule-based chatbot."
    elif "how are you?" in user_input:
        return "I'm just a program, but I'm here to help you!"
    elif "name" in user_input:
        return "My name is NANI."
    elif "who invented you?" in user_input:
        return "I was invented by Mr.NANI."
    elif "have a good day" in user_input:
        return "You too! Have a great day."
    elif "see you later" in user_input:
        return "See you later! Have a great day."
    elif "what are today's weather reports" in user_input:
        return "That's not my job."
    elif "how do you work" in user_input:
        return "I am a rule-based chatbot. I work based on the rules given by the user input."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."
    elif "what can you do" in user_input:
        return "I can answer simple questions and respond to basic greetings."
    elif "can you tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "what is the meaning of life" in user_input:
        return "The meaning of life is a philosophical question, but many believe it's to find happiness and purpose."
    elif "where are you from" in user_input:
        return "I exist in the digital realm, created by programmers."
    elif "tell me a fun fact" in user_input:
        return "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!"
    elif "do you like music" in user_input:
        return "As a chatbot, I don't have preferences, but music is fascinating!"
    elif "what is your favorite color" in user_input:
        return "I don't have a favorite color, but I think blue is quite popular."
    elif "how old are you" in user_input:
        return "I don't have an age, but I was created not too long ago!"
    elif "who is your creator" in user_input:
        return "I was created by Mr. deekshith."
    elif "can you help me with math" in user_input:
        return "Sure, I can try! What math problem do you need help with?"
    elif "what is your purpose" in user_input:
        return "My purpose is to assist you with simple queries and provide information."
    elif "do you have any hobbies" in user_input:
        return "I don't have hobbies, but I can tell you about various hobbies you might like!"
    else:
        return "I'm not sure how to respond to that."

# Main loop to interact with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")