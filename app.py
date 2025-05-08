import streamlit as st
import openai

# ✅ Replace with your real API key (keep private!)
openai.api_key = "sk-..."  # Paste your OpenAI API key here

st.title("🧠 Simple OpenAI Chatbot")
st.write("Talk to the bot!")

user_input = st.text_input("You:", "")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    st.write("🤖:", response.choices[0].message.content)


