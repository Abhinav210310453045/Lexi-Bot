import requests
import streamlit as st

def get_mistralai_response(input_text):
    json={'input':{'topic':input_text}}
    response=requests.post("http://localhost:8000/essay/invoke",json=json)
    # print(json)
    return response.json()['output']['content']


def get_ollama_response(input_text):
    json={'input':{'topic':input_text}}
    response=requests.post("http://localhost:8000/poem/invoke",json=json)
    return response.json()['output']

st.title("langchain bot with FastAPI")
input_text1=st.text_input("write an essay on")
input_text2=st.text_input("write a poem on")


if input_text1:
    st.write(get_mistralai_response(input_text1))
if input_text2:
    st.write(get_ollama_response(input_text2))


