import streamlit as st
from openai import OpenAI

# Use your actual API key here (only for local development!)
client = OpenAI(api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

st.title("💬 Chatbot with GPT-3.5")
st.markdown("Ask me anything!")

user_input = st.text_input("You:", "")

if user_input:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    chatbot_reply = response.choices[0].message.content
    st.write("Chatbot:", chatbot_reply)

