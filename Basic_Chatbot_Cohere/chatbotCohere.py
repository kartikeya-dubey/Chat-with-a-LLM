import streamlit as st
from dotenv import load_dotenv
import os
from langchain_community.llms import Cohere

# Load environment variables from .env file
load_dotenv()

# Access the COHERE_API_KEY environment variable
key = os.getenv("COHERE_API_KEY")

if key is None:
    raise ValueError("COHERE_API_KEY is not set in the .env file.")

#Establish connection with llm
llmModel = Cohere(cohere_api_key = key)

# Initialize chat history 
if "messages" not in st.session_state:
    st.session_state.messages = []

#chat histroy will be divided into 2 components: input prompt history + output response history
#Each entry in the list will be a dictionary with the following keys: role (the author of the message), and content (the message content).

#streamlit initiation page
    st.header("How may I help you?")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def main():

    #Customize GUI: create info sidebar
    with st.sidebar:
        st.header("Simple chat interface with LLM :speaking_head_in_silhouette:")
        st.subheader("Developed by Kartikeya Dubey")
        st.link_button(":link: LinkedIn","https://www.linkedin.com/in/kartikeyadubey/")
        st.link_button(":link: GitHub","https://github.com/kartikeya-dubey")
        
    
    #Accept chat from user
    prompt = st.chat_input("Ask me something!")
    if prompt:
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            #Supply prompt to llm
            response = llmModel(prompt)
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == '__main__':
    main()