def chatbot(input_text):
    # Convert input to lowercase for case-insensitive matching
    input_text = input_text.lower()

    # Define predefined responses based on user inputs
    if 'hello' in input_text:
        return "Hi there! How can I help you today?"

    elif 'how are you' in input_text:
        return "I'm just a bot, but thanks for asking!"

    elif 'bye' in input_text:
        return "Goodbye! Have a nice day."

    elif 'thank you' in input_text or 'thanks' in input_text:
        return "You're welcome!"

    else:
        return "Sorry, I don't understand that. Can you please rephrase or ask something else?"

