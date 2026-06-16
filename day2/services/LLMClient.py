from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv();

def CreateOpenAIClient():
    return OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"));

def CallLLM(client, messages:list, model_choice:str="gpt-4.1-mini", temperature:float=0.7):
    system_prompt = "You are a helpful assistant that provides concise and accurate answers to user queries.";
    response = client.chat.completions.create(
        model=model_choice,
        messages=messages + [{"role": "system", "content": system_prompt}],
        temperature=temperature, 
    );
    return response.choices[0].message.content;

def LLMResponse(user_query:str, model_choice:str="gpt-4.1-mini", temperature:float=0.7):
    client = CreateOpenAIClient();
    messages = [{"role": "user", "content": user_query}];
    return CallLLM(client, messages, model_choice, temperature);

if __name__ == "__main__":
    response = LLMResponse("Explore TechWayFit.com blogs and summarize in 3 lines?");
    print(response);