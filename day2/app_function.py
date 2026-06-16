
import os;
from dotenv import load_dotenv;
load_dotenv();
from openai import OpenAI;

def user_message(message:str):
    return {"role": "user", "content": message};
def system_message(message:str):
    return {"role": "system", "content": message};
def assistant_message(message:str):
    return {"role": "assistant", "content": message};

def call_llm(client, messages:list, model_choice:str="gpt-4.1-mini", temperature:float=0.7):
    system_prompt = "You are a helpful assistant that provides concise and accurate answers to user queries.";
    response = client.chat.completions.create(
        model=model_choice,
        messages=messages.append(system_message(system_prompt)),
        temperature=temperature, 
    );
    return response.choices[0].message;

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"));
messages=[];
while True: # C# Equivalent: while (true) {
    user_input = input("You: ");
    messages.append(user_message(user_input)); # C# Equivalent: messages.Add(user_message(user_input));
    llm_response = call_llm(client, messages);
    print(f"Assistant: {llm_response.content}");
    messages.append(llm_response); 
