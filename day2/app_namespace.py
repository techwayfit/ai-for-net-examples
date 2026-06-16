from services.LLMClient import CreateOpenAIClient, CallLLM, LLMResponse;


def user_message(message:str):
    return {"role": "user", "content": message};

client= CreateOpenAIClient();
response =  CallLLM(client, [user_message("What is the capital of France?")]);
print(response);

response = LLMResponse("How can .Net Dev can learn AI?");
print(response);


import services;
services.CallLLM;  # Accessing CallLLM directly from services package
print(services.LLM_BASE_URL);  # Accessing LLM_BASE_URL from services package