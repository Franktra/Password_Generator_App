import streamlit as st
import random
import string


def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if characters == "":
        st.write("Please select at least one character type.")
        return ""

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.title("Password Generator")

    length = st.slider("Password Length", min_value=6, max_value=20, value=10, step=1)
    include_uppercase = st.checkbox("Include Uppercase Letters")
    include_lowercase = st.checkbox("Include Lowercase Letters")
    include_numbers = st.checkbox("Include Numbers")
    include_special_chars = st.checkbox("Include Special Characters")

    if st.button("Generate Password"):
        password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
        st.write("Generated Password:", password)

if __name__ == "__main__":
    main()
