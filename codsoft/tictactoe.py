def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! I am your AI assistant. How can I help you today?"
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot created for my CodSoft internship!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a fantastic day ahead!"
    else:
        return "I'm sorry, I didn't quite catch that. Could you try phrasing it differently?"

print("Chatbot: Hello! Type 'bye' or 'exit' to leave the chat.")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print(f"Chatbot: {response}")
    
    if "bye" in user_message.lower() or "exit" in user_message.lower():
        break
