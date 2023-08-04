import streamlit as st
from main import MyApp

def main():
    app = MyApp()

    st.title("Conversation Chat with Swahili Videos")
    app.url = st.text_input("Enter the YouTube URL:")
    app.apikey = st.text_input("Enter OpenAI API Key:")
    st.write("Click 'Run' to start the chat.")

    if st.button("Run"):
        app.run()    


if __name__ == "__main__":
    main()