import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found.")

client = Groq(api_key=my_api_key)
model = "llama3-8b-8192"

messages = [
    {"role": "user", "content": "Do you know who is Yuvanshi Bhalawat?"}
]

response = client.chat.completions.create(model=model, messages=messages)

print("####################")
print("Assistant reply:", response.choices[0].message.content)
print("Token usage:", response.usage)
