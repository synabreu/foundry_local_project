import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from foundry_local import FoundryLocalManager


# 별칭(alias) 사용. 사용 가능한 모델 목록을 확인하려면,  foundry model list
alias = "phi-3-mini-4k"

# FoundryLocalManager 인스턴스 생성 
# Foundry Local 서비스가 아직 실행 중이 아니라면 서비스를 시작하고, 지정된 모델을 로드함
manager = FoundryLocalManager(alias)

# ChatOpenAI를 로컬 PC/Mac에서 실행 중인 모델을 사용하도록 구성함
llm = ChatOpenAI(
    model=manager.get_model_info(alias).id,
    base_url=manager.endpoint, 
    api_key=manager.api_key,
    temperature=0.8,
    streaming=False
)

# 번역 프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant that translates {input_language} to {output_language}."
    ),
    ("human", "{input}")
])

# 프롬프트를 언어 모델에 연결하여 간단한 체인 생성
chain = prompt | llm

input = "J'aime coder."
print(f"'{input}'를 우리나라 말로 번역중...")

# 입력값을 사용해 체인 실행
ai_msg = chain.invoke({
    "input_language": "French",
    "output_language": "Korean",
    "input": input
})

# 결과 컨텐트 출력
print(f"응답 결과: {ai_msg.content}")