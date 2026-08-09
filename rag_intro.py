import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"

#step 1: knowledge base ready kro
knowledge_base={
    "What is Yuvi?": "Yuvi is a nickname of Yuvanshi Bhalawat, final year engineering student.",
    "Age": "Yuvi is 21 years old."
    
}

#step 2 : retrive on knowledge base
def retrieve_info(question):
    question = question.lower()
    if "age" in question:
        return knowledge_base["Age"]
    elif "yuvi" in question:
        return knowledge_base["What is Yuvi?"]
    else:
        return "Sorry, I don't have information on that."
    

def ask_llm(question):
    context = retrieve_info(question)
    sys_prompt = f"You are a helpful assistant that provides accurate and concise answers to questions. Answer only based on this context: {context}"
    
    system_message = {
        "role":"system",
        "content": sys_prompt     
    }
    message = {
        "role": "user",
        "content" : question
    }
    messages = [system_message, message]
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer

question= "yuvi ki age kya  hai?"
print(ask_llm(question))

    