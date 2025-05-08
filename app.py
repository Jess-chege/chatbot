import streamlit as st

# Define responses for user inputs
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
    "tell me a joke": "Sure! Why don't skeletons fight each other? They don't have the guts! 😄",
    "default": "Sorry, I didn't quite get that. Try asking something else!"
}

# Basic chatbot logic to get responses
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]

# Streamlit app setup
st.set_page_config(page_title="ChatBot", page_icon=":robot_face:", layout="wide")

# Custom header
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>Welcome to Your Personal Chatbot</h1>
    <p style='text-align: center; color: #607D8B;'>Let's chat! I'm here to assist you with simple responses and fun conversations.</p>
""", unsafe_allow_html=True)

# Initialize the chat history to keep track of the conversation
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input: Text area to allow more space to type messages
user_input = st.text_area("You:", "", height=200, key="input", max_chars=500)

# If the user has typed something, process the input
if user_input:
    bot_response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

# Display the ongoing chat conversation
for speaker, message in st.session_state.chat_history:
    st.write(f"**{speaker}:** {message}")

