import streamlit as st

# Define basic responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "help": "You can ask me about basic things like 'hello', 'how are you', or say 'bye'."
}

# Basic chatbot logic
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm not sure how to respond to that. Try saying 'help'."

# Streamlit app
st.title("Simple Chatbot (No OpenAI)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", key="input")

if user_input:
    bot_response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    st.write(f"**{speaker}:** {message}")


