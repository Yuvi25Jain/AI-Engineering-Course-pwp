import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="I love you baby" 

# prompt = "Suggest me a good name"

#day 2 : sending one more message_system : system role
message_system={
    "role": "system",
    "content": "TED talk speaker"
}
#temperature
# message_system={
#     "role": "system",
#     "content": "You are a brand manager , suggest me a good name for my new product in one word"
# }


# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system , message]

# add temperature parameter
response=client.chat.completions.create(model=model, messages=messages , temperature= 0.8)
# print(response)      //day 2 changes 

print("#######################################")

answer=response.choices[0].message.content
print(answer)


# code is same as day 1 with the following changes.

# 1. always import groq and dotenv file : how ?   uv add python-dotenv , uv add groq
#2. prompt accordingly
#3. new dictionary message_system = {
#     "role": "system",
#     "content": "TED talk speaker"
# }
#4. in message array . pass message_system as well
#5. to set temparature response = client wali line me after messages , add temperature parameter as temperature = (between 0 to 1) , higher the number higher will be the creativity.

