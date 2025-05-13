class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 길이가 짝수일 때
        # 현재 문자열 기준 같은 문자열이 연달아 나와야 함.
        # 길이가 홀수일 때
        # 중앙 기준 양옆이 같아야 함.
        
        # 투 포인터 활용
        # 각 문자열을 기준으로 투 포인터로 중심 확장하기
        start, end = self._get_max_palindrome(s)
        return s[start:end + 1]

    def _get_max_palindrome(self, s: str) -> Tuple[int, int]:
        max_start, max_end = 0, 0
        for i in range(len(s)):
            for dr in (0, 1):  # 홀수, 짝수 중심
                left, right = self._expand_from_center(s, i, i + dr)
                if right - left > max_end - max_start:
                    max_start, max_end = left, right
        return max_start, max_end

    def _expand_from_center(self, s: str, left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1