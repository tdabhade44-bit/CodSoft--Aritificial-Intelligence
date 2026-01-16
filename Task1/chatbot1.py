print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hi there! How can I help you?")
    
    elif "how are you" in user_input:
        print("Chatbot: I am fine! Thank you for asking.")
    
    elif "your name" in user_input:
        print("Chatbot: I am a rule-based chatbot created for CodSoft AI internship.")
    
    elif "help" in user_input:
        print("Chatbot: I can answer basic questions like greetings or my name.")
    
    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day")
        break
    
    else:
        print("Chatbot: Sorry, I didn't understand that.")
