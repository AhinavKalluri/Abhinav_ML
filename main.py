import os
from mistralai import Mistral 
from dotenv   import load_dotenv 
load_dotenv()
x=input('What You Want to Know : ')

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": x,
        },
    ]
)

print(chat_response.choices[0].message.content)