# Hacivat

Hacivat is a scarcastic chatbot that are trained by `cornell_movie_dialogs_corpus`. Additionally we trained by dialogs that my wife and I created. WE realized that jokes and conversations are shaped more sarcartic mennor that we can use those an chatbot AI.
Model has been built in another gitguh repo which is available []()


## Installation

Tool can be used any other package by install it via git command

```bash
poetry add git+https://github.com/caglanakpinar/hacivat.git
```

## Requirements

model will available on other framwork that is available on [chatbot_transformer](https://github.com/caglanakpinar/chatbot_transformer)
please take a look at `read.me`. To run hacivat, download  [chatbot_transformer](https://github.com/caglanakpinar/chatbot_transformer), and run below lines in  `chatbot_transformer`
```
poetry install 
poetry run python3 api.py 
```


# Run

* `streamlit run app/chat.py` - run interface
* you can use by `<internal IP>:8501` within same network, or local `0.0.0.0:8501`


# Interface

![alt Screenshot](https://github.com/user-attachments/assets/abef0651-7d0d-41bd-b614-f8e39d116b06)

* `please enter your answer you like!`
  * if you don't like previous answer, you can change by adding your answer to this section. Model will take your answer seriously and will train the model behind, based on your answer. So, you probably have your version of `Hacivat`.

