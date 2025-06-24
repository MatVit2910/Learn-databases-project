import os

from groq import Groq
import requests

STOCK_DATA_API_KEY = os.environ.get('STOCK_DATA_API_KEY')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

params = {'api_token':STOCK_DATA_API_KEY, 'industries':'Technology', 'language' : 'en'}
r = requests.get('https://api.stockdata.org/v1/news/all', params=params)

client = Groq(
    api_key=GROQ_API_KEY,
)

inp = input("What would you like to ask?\n")

chat_completion = client.chat.completions.create(
    messages=[
        {
        "role": "system",
        "content": "You are a financial advisor. Keep your responses as concise as possible."
      },
      {
        "role": "user",
        "content": inp + str(r.json())
      }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)

