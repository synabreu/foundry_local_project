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
            "content": "What is Windows Foundry Local on Microsoft?",
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "INSERT_INPUT_HERE",
                },
            ],
        },
    ],
    model = "Phi-4-mini-cpu-int4-rtn-block-32-acc-level-4-onnx",
    max_tokens = 256,
    temperature = 0.8,
    top_p = 1,
    frequency_penalty = 1,
)

print(response.choices[0].message.content)