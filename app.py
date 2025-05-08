import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Use Streamlit secrets for safety

st.title("💬 Simple Chatbot with OpenAI")
st.markdown("Ask me anything!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Call OpenAI API
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages,
        )
        reply = response.choices[0].message["content"]

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)


