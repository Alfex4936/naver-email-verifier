import base64

import httpx


class NaverChecker:
    """
    네이버 이메일 사용자 ID 사용 여부를 확인하는 클래스입니다.

    이 클래스의 인스턴스는 내부적으로 `httpx.Client`를 사용하여 네이버에 HTTP 요청을 보냅니다.
    클라이언트는 인스턴스가 소멸될 때까지 오픈 상태로 유지되며, 모든 요청에 대해 10초의 타임아웃이 설정됩니다.

    이메일 ID가 이미 사용 중이라면 `is_id_in_use` 메소드는 `True`를 반환합니다.
    하지만 이 결과가 100% 정확하다고 테스트는 못했으며, 일반적으로 잘 작동하는 것으로 확인되었습니다.

    SMTP로 이메일 보내기 전에 간단하게 체크하기 좋습니다.

    사용 예:
    ```python
    checker = NaverChecker()
    is_used = checker.is_id_in_use("example_user_id")
    print("존재하는 계정 입니다." if is_used else "존재 하지 않는 계정 입니다.")
    ```
    """

    def __init__(self):
        dbase = base64.b64decode(b"aHR0cHM6").decode("utf-8")
        c1 = base64.b64decode(b"Ly9uaWQubmF2ZXIuY29tL3Vz").decode("utf-8")
        c3 = base64.b64decode(b"ZXIyL2pvaW5BamF4").decode("utf-8")
        base_url = dbase + c1 + c3

        self.base_url = base_url
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        self.client = httpx.Client(timeout=10.0)
        self.async_client = httpx.AsyncClient(timeout=10.0)

    def is_id_in_use_sync(self, user_id, user_agent=None):
        """Synchronously checks the availability of a user ID."""
        if user_agent is None:
            user_agent = self.user_agent
        if self.client.is_closed:
            self.client = httpx.Client(timeout=10.0)

        if "@naver.com" in user_id:
            user_id = user_id.split("@naver.com")[0]

        response = self.client.get(
            self.base_url,
            headers={"User-Agent": user_agent},
            params={"m": "checkId", "id": user_id},
        )
        return response.text.strip().endswith("N")

    async def is_id_in_use_async(self, user_id, user_agent=None):
        """Asynchronously checks the availability of a user ID."""
        if user_agent is None:
            user_agent = self.user_agent
        if self.async_client.is_closed:
            self.async_client = httpx.AsyncClient(timeout=10.0)

        if "@naver.com" in user_id:
            user_id = user_id.split("@naver.com")[0]

        response = await self.async_client.get(
            self.base_url,
            headers={"User-Agent": user_agent},
            params={"m": "checkId", "id": user_id},
        )
        return response.text.strip().endswith("N")
