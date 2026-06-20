from services.LLMClient import *;


def user_message(message:str):
    return {"role": "user", "content": message};

client= create_llm_client();
response =  _call_llm(client, [user_message("What is the capital of France?")]);
print(response);

response = llm_response("How can .Net Dev can learn AI?");
print(response);


import services;
services.CallLLM;  # Accessing CallLLM directly from services package
print(services.LLM_BASE_URL);  # Accessing LLM_BASE_URL from services package