
import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('GuardianAngels')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@st.cache(allow_output_mutation=True)
def get_chatbot():
    return ChatBot('GuardianAngels')

def get_response(user_input):
    chatbot = get_chatbot()
    response = chatbot.get_response(user_input)
    return str(response)

def main():
    st.title('Chatbot Demo')
    user_input = st.text_input('User Input')

    if st.button('Submit'):
        response = get_response(user_input)
        st.text_area('Bot Response', value=response)

if __name__ == '__main__':
    main()
