from .LLMClient import CallLLM; 
import os;
from dotenv import load_dotenv;
load_dotenv();
print("initializing services package...");

LLM_BASE_URL = os.getenv("BASE_URL");