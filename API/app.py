from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import OllamaLLM  # Updated import for Ollama
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="This is a simple API"
)


mistral_model = ChatMistralAI()
ollama_model = OllamaLLM(model="llama3.2:1b")

prompt1 = ChatPromptTemplate.from_template("write an essay about {topic} with 100 words.")
prompt2 = ChatPromptTemplate.from_template("write me a poem about {topic} with 100 words.")

add_routes(app, mistral_model, path="/MistralAi")
add_routes(app, prompt1 | mistral_model, path="/essay")
add_routes(app, prompt2 | ollama_model, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
