
# add chat memory
# use a local server like streamlit
#/ modify streamlit with html to make a nice looking chat bot
#/ user longchain framework to read .pdf files
#/ use a open source LLM that doesn't cost tokens


import streamlit as st
import openai


openai.api_key = ""


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful Python tutor."}
    ]


st.title("Python Study Chatbot")


user_input = st.text_input("You:", "")


if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )


    reply = response["choices"][0]["message"]["content"]

    # Save assistant's message to history
    st.session_state.messages.append({"role": "assistant", "content": reply})


for msg in st.session_state.messages[1:]: 
    speaker = "You" if msg["role"] == "user" else "Bot"
    st.markdown(f"**{speaker}:** {msg['content']}")
