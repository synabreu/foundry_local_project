"""Run this model in Python

> pip install openai
"""
from openai import OpenAI

client = OpenAI(
    base_url = "http://localhost:5272/v1/",
    api_key = "unused", # required for the API but not used
)

response = client.chat.completions.create(
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Who is the CEO of Microsoft?",
                },
            ],
        },
    ],
    model = "Phi-4-mini-gpu-int4-rtn-block-32",
    max_tokens = 256,
    temperature = 0.8,
    frequency_penalty = 1,
)

print(response.choices[0].message.content)