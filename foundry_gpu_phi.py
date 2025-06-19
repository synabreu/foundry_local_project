"""Run this model in Python

> pip install azure-ai-inference
"""
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage, ToolMessage
from azure.ai.inference.models import ImageContentItem, ImageUrl, TextContentItem
from azure.core.credentials import AzureKeyCredential

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = ChatCompletionsClient(
    endpoint = "https://models.inference.ai.azure.com",
    credential = AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages = [
        UserMessage(content = [
            TextContentItem(text = "Who is the CEO of Microsoft?"),
        ]),
    ],
    model = "Phi-4-mini-instruct",
    temperature = 0.8,
    top_p = 0.1,
)

print(response.choices[0].message.content)
