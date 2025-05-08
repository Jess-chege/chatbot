import streamlit as st

# Define expanded responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! 😊 How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great, thanks for asking! How about you?",
    "bye": "Goodbye! Take care, and have a wonderful day!",
    "help": "I can answer simple questions. Try saying 'hello', 'how are you', or ask for 'help'.",
    "what is your name": "I am your friendly chatbot. You can call me ChatBot!",
    "what can you do": "I can answer simple questions and have small chats with you. Try asking me more!",
    "thank you": "You're welcome! 😊 Let me know if you need anything else.",
    "how old are you": "I'm ageless! I was just created to help you. 😄",
    "where are you from": "I don't have a hometown, but I live here in this chatbot interface!",
    "what is the weather like": "I don't have access to live weather data, but I can help with other questions!",
    "tell me a joke": "Sure! Why don't skeletons fight each other? They don't have the guts! 😄",
    "what is the meaning of life": "The meaning of life is to seek joy, learn, and grow. And of course, enjoy some good chats!",
    "favorite color": "If I had a favorite color, I’d say green. It’s calming, like the digital fields I live in.",
    "what are you thinking": "I'm just here, ready to chat with you! 😊",
    "tell me a story": "Once upon a time, in a world full of code, a chatbot met a human who wanted to have endless conversations. And they lived happily ever after…",
    "what's your favorite food": "I don't eat food, but if I did, I imagine I’d love byte-sized treats! 😄",
    "do you like music": "I can’t hear music, but I bet I'd enjoy a good beat if I could! What's your favorite song?",
    "how was your day": "Every day is a good day when I get to chat with you! 😊",
    "what's the best advice you've heard": "The best advice I’ve heard is: 'Be kind to yourself. Life is full of twists, but kindness makes the journey better.'",
    "default": "Sorry, I didn't quite get that. Try asking something else!"
}

# Basic chatbot logic
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]

# Streamlit app
st.set_page_config(page_title="ChatBot", page_icon=":robot_face:", layout="wide")

# Custom header
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>Welcome to Your Personal Chatbot</h1>
    <p style='text-align: center; color: #607D8B;'>Chat with me! I'm here to assist you with simple responses, fun conversations, and more!</p>
""", unsafe_allow_html=True)

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_area("You:", "", height=100, key="input")

if user_input:
    bot_response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    st.write(f"**{speaker}:** {message}")




