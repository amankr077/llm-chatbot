import streamlit as st
import requests
import os

st.title("My LLM Chatbot")

user_input = st.text_input("Ask me anything:")

# Get API key securely from Streamlit Secrets or environment variables
API_KEY = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))

if st.button("Send") and user_input:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.2,
    }

    response = requests.post(url, headers=headers, json=payload)

    try:
        reply = response.json()["choices"][0]["message"]["content"]
        st.write(reply)
    except Exception as e:
        st.error("Something went wrong. Full response below:")
        st.json(response.json())
