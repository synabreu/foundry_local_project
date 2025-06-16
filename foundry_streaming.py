import openai
from foundry_local import FoundryLocalManager


# 모델 별칭(alias) 사용
alias = "phi-3-mini-4k"

### 1. FoundryLocalManager 인스턴스를 생성 ###

# Foundry Local 서비스가 아직 실행 중이 아니라면, 서비스를 시작하고 alias로 지정된 모델을 로드함
manager = FoundryLocalManager(alias)

### 2. OpenAI Python SDK를 사용하여 로컬 모델과 상호작용함 ###

# 클라이언트를 PC나 MacOS와 같은 로컬 Foundry 서비스를 사용하도록 구성함
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key  # 로컬에서 사용할 경우 API 키는 필요하지 않음
)

# 사용할 모델을 설정하고 streaming 응답을 생성함
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is Microsoft Foundry Local?"}],
    stream=True
)

# streaming 응답 출력
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)