import os;
from dotenv import load_dotenv;
load_dotenv();
from openai import OpenAI;

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"));

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)
print(response.choices[0].message.content);
