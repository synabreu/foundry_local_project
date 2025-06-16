"""Run this model in Python

> pip install openai
"""
import os
from openai import OpenAI
from dotenv import load_dotenv


# .env 파일에서 환경 변수 불러오기
load_dotenv()

# 환경 변수 가져오기
github_token = os.getenv("GITHUB_TOKEN")

if github_token is None:
    raise ValueError("GITHUB_TOKEN이 설정되어 있지 않습니다.")

# 모델에 인증하려면 GitHub 설정에서 \*\*개인 액세스 토큰(PAT)\*\*을 생성해야 함
# 아래 링크의 안내를 따라 PAT 토큰을 생성하세요: [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
client = OpenAI(
    base_url = "https://models.inference.ai.azure.com",
    api_key = github_token,
    default_query = {
        "api-version": "2024-08-01-preview",
    },
)

response = client.chat.completions.create(
    messages = [
        {
            "role": "system",
            "content": "Summarize the provided text into a concise overview capturing the main ideas and key information.\n\n- Focus on retaining the essential details while eliminating unnecessary information.\n- Ensure the summary is coherent and flows logically.\n\n# Steps\n\n1. Read the text carefully.\n2. Identify the main ideas and supporting details.\n3. Eliminate redundancy and irrelevant information.\n4. Rewrite the main points in your own words to create a coherent summary.\n\n# Output Format\n\nThe summary should be one paragraph, approximately 3-5 sentences long.\n\n# Examples\n\nInput: \"The cat is a domestic species of carnivorous mammal. It is often kept as a pet and is valued for its companionship and ability to hunt pests. Cats are known for their agility and playful behavior, making them popular in households around the world.\"\n\nOutput: \"Cats are domesticated carnivorous mammals valued for companionship and pest control. Known for their agility and playful nature, they are popular pets globally.\"\n\nInput: \"[Insert another example text here for summarization]\"\n\nOutput: \"[Insert the expected summary output here]\" \n\n# Notes\n\n- Avoid including personal opinions or interpretations in the summary.\n- The summary should only reflect the content of the original text without additional commentary or insights.",
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is Agentic AI?",
                },
            ],
        },
    ],
    model = "gpt-4o-mini",
    tools = [],
    response_format = {
        "type": "text"
    },
    temperature = 1,
    top_p = 1,
)

if response.choices[0].message.tool_calls:
    print(response.choices[0].message.tool_calls)
else:
    print(response.choices[0].message.content)
