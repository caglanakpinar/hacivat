import streamlit as st
import requests
import json
from datetime import datetime

from utils import Paths



class Bot:
    url = 'http://0.0.0.0:8384'

    @staticmethod
    def executable(prompt):
        return  prompt[0] == '|'

    def trainable(self, prompt):
        prompt = prompt[1:].lower().split()
        if len(prompt) == 1 and prompt[0] == 'train':
            self.train_yourself()
        if prompt[0] == 'train' and prompt[1] == 'me':
            self.train_yourself()

    def add_chat_history(self, chat_history_files, date):
        data = json.dumps({"files": chat_history_files, "date": date})
        r = requests.get(self.url+"/files", data=data)

    def answer_me(self, prompt):
        if self.executable(prompt):
            self.trainable(prompt)
            return "I updated myself. New, fresh world! :)"
        else:
            data = json.dumps({"prompt": prompt})
            r = requests.get(self.url, data=data)
            return json.loads(r.text)['output']

    def train_yourself(self):
        r = requests.get(self.url+"/train")


class ChatCollect(Paths, Bot):
    cache_files = []
    cache = []
    chat_history_pre_line_cnt = 10
    total_cache_files = 1000

    def get_cache_time(self):
        return (
            str(datetime.now())
            .replace("-", "")
            .replace(":", "")
            .replace(" ", "")
            .replace(".", "")
        )

    def write_cache_message(self, file):
        with open(file, "w") as f:
            for message in self.cache:
                for key, value in message.items():
                    f.write('%s:%s\n' % (key, value))
        f.close()
        self.cache = []


    def caching(self, messages):
        if len(messages) % self.chat_history_pre_line_cnt == 0 and len(messages) != 0:
            self.cache = messages[-10:]
            _file = self.data_path / f"{self.get_cache_time()}.txt"
            self.cache_files.append(_file)
            self.write_cache_message(_file)
            if len(self.cache_files) == self.total_cache_files:
                self.add_chat_history(self.cache_files, self.get_cache_time())
                self.cache_files = []
                self.remove_files_in_data()


bot = Bot()
collector = ChatCollect()


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

    collector.caching(st.session_state.messages)
    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):

            st.markdown(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = bot.answer_me(prompt)
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == '__main__':
    interface()