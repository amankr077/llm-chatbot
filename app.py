import streamlit as st
import requests

st.title("Aman LLM Chatbot")

user_input = st.text_input("Ask me anything:")

if st.button("Send") and user_input:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": "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",  # <- Add your key here
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.2,
    }
    response = requests.post(url, headers=headers, json=payload)
    reply = response.json()["choices"][0]["message"]["content"]
    st.write(reply)
