import openai
from django.conf import settings


def get_gpt_response(prompt):
    openai.api_key= settings.CHATGPT_KEY
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()