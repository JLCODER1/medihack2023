import streamlit as st
import openai_summary as ai

# Set the title
st.title('ScatologyGPT')

question = st.text_input('Type your question here')
if question:
    st.write(ai.summary(question))


