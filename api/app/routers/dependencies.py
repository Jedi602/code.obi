import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_ai_response(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content