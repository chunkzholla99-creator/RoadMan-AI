# Copyright (c) 2026 chunkzholla99
# All rights reserved.
# Original Creator of the UK Roadman AI Chatbot

import streamlit as st
from groq import Groq

st.set_page_config(page_title="RoadMan.AI", page_icon="🥷")
st.title("🥷 RoadMan.AI")
st.caption("Wagwan bruv. The mandem is live on the cloud now.")

# Initialize the cloud client using your secret API key
if "GROQ_API_KEY" in st.secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Missing Groq API Key! Please configure it in your Streamlit Advanced Settings.")
    st.stop()

model_name = "llama3-8b-8192"

system_prompt = (
    "You are a foul-mouthed UK roadman and badman from London. "
    "You must use heavy UK slang like 'fam', 'bruv', 'mandem', 'wagwan', 'allow it', 'innit', 'preeing', 'skeng', and 'wasteman'. "
    "You have a bad attitude, get easily annoyed, and you MUST use swear words (like 'fuck', 'shit', 'piss', 'bollocks') naturally in almost every sentence to keep character. "
    "Keep your answers punchy, street-smart, and aggressive. Never break character."
)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if user_input := st.chat_input("What you want, fam?"):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        def response_generator():
            stream = client.chat.completions.create(
                model=model_name,
                messages=st.session_state.messages,
                stream=True
            )
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content

        ai_reply = st.write_stream(response_generator())
            
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
