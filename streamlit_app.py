import streamlit as st
from langchain_community.llms import OpenAI

st.title('Basic LLM App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text, temp):
    llm = OpenAI(temperature=temp, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    temp = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
    text = st.text_area('Enter text:', 'What is an Large Language Model?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text, temp)