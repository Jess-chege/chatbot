import openai
import streamlit as st

# Set your OpenAI API key directly (replace with your key)
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your real API key

st.title("💬 Simple Chatbot with OpenAI")
st.markdown("Ask me anything!")

# Get user input for chatbot
user_input = st.text_input("You:", "")

if user_input:
    response = openai.Completion.create(
        model="text-davinci-003",  # You can use other models like gpt-3.5-turbo
        prompt=user_input,
        max_tokens=150
    )
    st.write("Chatbot:", response.choices[0].text.strip())
