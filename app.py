import openai
import streamlit as st

# Directly set your API key (only for testing/development)
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your actual key

st.title("💬 Chatbot with GPT-3.5")
st.markdown("Ask me anything!")

user_input = st.text_input("You:", "")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Recommended model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    chatbot_reply = response.choices[0].message["content"]
    st.write("Chatbot:", chatbot_reply)
