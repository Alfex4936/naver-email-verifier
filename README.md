# NaverChecker

`NaverChecker`는 네이버 이메일 사용자 ID의 사용 여부를 확인하는 파이썬 라이브러리입니다.

이 라이브러리는 내부적으로 `httpx.Client`를 사용하여 네이버 API에 HTTP 요청을 보내어,

해당 네이버 이메일 ID가 존재하는지를 확인합니다.

## 설치 방법

패키지를 설치하려면 다음 pip 명령어를 사용합니다:

```bash
pip install naver_email_verifier
```

## 사용 예제

`NaverChecker`를 사용하여 이메일 ID의 사용 여부를 확인하는 방법은 다음과 같습니다.

**동기 및 비동기 지원**: 사용자의 요구에 맞게 동기 또는 비동기 방식을 선택할 수 있습니다.

```python
from naver_email_verifier import NaverChecker

# 동기 방식
naver_checker = NaverChecker()
is_used = naver_checker.is_id_in_use_sync("example_user_id")
print("존재하는 계정입니다." if is_used else "존재하지 않는 계정입니다.")

# 비동기 방식
import asyncio

async def check_async():
    is_used = await naver_checker.is_id_in_use_async("seokwon84354")
    print("존재하는 계정입니다." if is_used else "존재하지 않는 계정입니다.")

asyncio.run(check_async())
```

## 리소스 해제

HTTP 클라이언트는 인스턴스가 소멸될 때까지 오픈 상태로 유지되며 인스턴스를 삭제하면 닫힙니다.