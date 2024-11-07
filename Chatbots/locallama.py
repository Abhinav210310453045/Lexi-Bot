from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
# from langchain.llms import ollama
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os 
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant ,provide brief and short answers to the questions"),
        ("user","Question:{question}")
    ]
)
st.title("Langchain Bot using OLLAMA")
input_text=st.text_input("search your query")

llm=Ollama(model="llama3.2:1b")
output=StrOutputParser()
chain = prompt|llm|output

if(input_text):
    st.write(chain.invoke({"question":input_text}))


