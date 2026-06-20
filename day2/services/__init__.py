from .LLMClient import create_llm_client, llm_response; 
import os;
from dotenv import load_dotenv;
load_dotenv();
print("initializing services package...");

LLM_BASE_URL = os.getenv("BASE_URL");

__all__ = ["create_llm_client", "llm_response", "LLM_BASE_URL"];