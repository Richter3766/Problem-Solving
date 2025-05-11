class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        dictionary를 활용하는 방식이 먼저 떠오름.
        슬라이딩 윈도우를 활용하여 N의 속도 목표
        """
        
        char_dict = {} # 문자가 마지막으로 등장한 인덱스를 저장함.
        left = 0
        max_length = 0

        for right in range(len(s)):
            cur_char = s[right] # 현재 문자열

            # 중복되는 문자열이 현재 윈도우에 있을 경우
            if cur_char in char_dict and char_dict[cur_char] >= left:
                left = char_dict[cur_char] + 1 # 윈도우 위치를 옮겨줌.

            char_dict[cur_char] = right # 현재 문자가 마지막으로 등장한 인덱스로 저장

            max_length = max(max_length, right - left + 1) # 현재 최대 길이 업데이트
        
        return max_length
