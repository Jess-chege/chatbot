import streamlit as st
from openai import OpenAI

# ✅ Replace this with your real API key
client = OpenAI(api_key="sk-...")

st.title("🧠 Simple Chatbot")
st.write("Talk to the bot!")

user_input = st.text_input("You:", "")

if user_input:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    st.write("🤖:", response.choices[0].message.content)


