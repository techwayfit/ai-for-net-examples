import os;
from dotenv import load_dotenv;
load_dotenv();
from openai import OpenAI;

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"));
messages=[];
USER_COLOR = "\033[93m";
ASSISTANT_COLOR = "\033[96m";
ASSISTANT_TEXT_COLOR = "\033[92m";
RESET_COLOR = "\033[0m";

supported_models = ["gpt-4.1-mini", "gpt-4.1", "gpt-4.1-pro"];
print(f"Supported models: {', '.join(supported_models)}");  # C# Equivalent: "Supported models: {string.Join(", ", supported_models)}");
model_choice = input("Choose a model: ");





while True: # C# Equivalent: while (true) {
    user_input = input(f"{USER_COLOR}You:{RESET_COLOR} ");
    messages.append({"role": "user", "content": user_input}); 
    # C# Equivalent: messages.Add(new KeyValuePair<string, string> { { "role", "user" }, { "content", user_input } });
    response = client.chat.completions.create(
        model=model_choice,
        messages=messages
    );
    assistant_message = response.choices[0].message;
    print(f"{ASSISTANT_COLOR}Assistant:{RESET_COLOR} {ASSISTANT_TEXT_COLOR}{assistant_message.content}{RESET_COLOR}");
    messages.append(assistant_message); # C# Equivalent: messages.Add(assistant_message);
