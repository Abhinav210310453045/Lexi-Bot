from langchain_mistralai import ChatMistralAI
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
os.environ["MISTRAL_API_KEY"]=os.getenv("MISTRAL_API_KEY")
# langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a creative assistant, please give answer in witty way,behave like a joker"),
        ("user","Question:{question}")
    ]
)
st.title("LangBot")
input_text=st.text_input("Speak  with the LangBot")
#invokig the mistral api

llm=ChatMistralAI(model="mistral-large-latest")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))