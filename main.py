from naver_email_verifier.verifier import NaverChecker

naver_checker = NaverChecker()

# Synchronous use
for idz in ("testuser123", "unique", "seokwon658451@naver.com"):  # T, T, F
    is_valid_naver_email = naver_checker.is_id_in_use_sync(idz)
    print(f"{idz} result: {is_valid_naver_email}")

# Asynchronous use
import asyncio  # noqa: E402


async def run():
    is_valid_naver_email = await naver_checker.is_id_in_use_async("naver")
    print("Async result:", is_valid_naver_email)  # True? 존재하는 이메일임, 보내도 좋음


if __name__ == "__main__":
    asyncio.run(run())
