import streamlit as st

def chatbot_response(user_input):
    # Define your chatbot logic here
    if user_input.lower() == "hello":
        return "Hi! How can I assist you?"
    elif user_input.lower() == "goodbye":
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase?"

def main():
    st.title("Chatbot")
    st.write("Welcome! Enter your message below.")

    user_input = st.text_input("User Input:")
    submit_button = st.button("Submit")

    if submit_button:
        bot_response = chatbot_response(user_input)
        st.write("Bot Response:", bot_response)

if __name__ == "__main__":
    main()
