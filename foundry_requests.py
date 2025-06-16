# requests 라이브러리 설치(pip install requests)
import requests
import json
from foundry_local import FoundryLocalManager

### 1. FoundryLocalManager 인스턴스를 생성 ###

# Foundry Local 서비스가 아직 실행 중이 아니라면, 서비스를 시작하고 alias로 지정된 모델을 로드함
alias = "phi-3-mini-4k"

### 2. OpenAI Python SDK를 사용하여 로컬 모델과 상호작용함 ###

# 클라이언트를 PC나 MacOS와 같은 로컬 Foundry 서비스를 사용하도록 구성함
manager = FoundryLocalManager(alias)

# URL은 OpenAI Chat API와 유사한 RESTful 인터페이스
# FoundryLocalManager에서 얻은 로컬 서버의 API 엔드포인트(http://localhost:8080 등)에 /chat/completions 경로를 붙여서 대화형 모델 호출 URL을 완성함
url = manager.endpoint + "/chat/completions"

# HTTP POST 요청에 담을 JSON 본문(body)
# model: 사용할 모델 ID (phi-3-mini-4k와 같은 모델의 내부 식별자)
# messages: 사용자 메시지를 대화 형식으로 전달함. 
# role이 "user"이면 사용자 입력이며, 시스템 메시지나 assistant 응답도 추가할 수 있음
payload = {
    "model": manager.get_model_info(alias).id,
    "messages": [
        {"role": "user", "content": "What is HTTP requests?"}
    ]
}

# HTTP 요청의 헤더 설정으로, JSON 포맷임을 명시함
headers = {
    "Content-Type": "application/json"
}

# 위의 URL에 POST 요청을 보내고, data=json.dumps(payload)를 통해 payload를 문자열로 직렬화하여 전송함
# Foundry Local이 해당 모델을 실행하여 응답을 생성함
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json()["choices"][0]["message"]["content"])