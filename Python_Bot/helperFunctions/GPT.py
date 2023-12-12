from openai import OpenAI
from decouple import config

client = OpenAI(
    api_key = config('GPT_KEY')
)

def askGPT(prompt):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = prompt,
        max_tokens = 60
    )

    return response.choices[0].message.content.strip()