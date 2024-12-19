import streamlit as st
import requests
import json

from utils import Paths


def interface():
    st.set_page_config(page_title='hacivat', page_icon='🐍')

    st.header("hacivat")
    st.image(
        str(Paths.parent_dir / "app/hacivat.png"),
        width=200
    )

    with st.sidebar:
        st.write("please enter your answer you like!")
        st.chat_input("please enter your answer you like!")


    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    with st.container(border=True, height=300):
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            url = 'http://0.0.0.0:8384'
            data = json.dumps({"prompt": prompt})
            r = requests.get(url, data=data)
            response = json.loads(r.text)['output']
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == '__main__':
    interface()