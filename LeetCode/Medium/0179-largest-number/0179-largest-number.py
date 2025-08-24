class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 1) 문자열 변환
        strs = list(map(str, nums))

        # 2) key 함수 정의
        # 문자열을 충분히 반복해서 비교 기준으로 사용
        # 예: "3" -> "3333333333" / "30" -> "3030303030"
        # 문자열은 숫자와 다르게 자릿수별 사전식으로 비교함
        strs.sort(key=lambda x: x*10, reverse=True)

        # 3) 모두 0인 경우 처리
        if strs[0] == "0":
            return "0"

        # 4) 이어붙여 반환
        return "".join(strs)