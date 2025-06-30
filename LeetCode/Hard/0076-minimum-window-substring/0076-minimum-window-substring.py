from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        두 개의 문자열 s, t
        각각의 길이는 m, n
        t의 모든 문자를 포함하는 최소 윈도우 문자열 찾기
        없으면 "" 반환

        t 안에 중복 문자열이 있을 경우 'aa' s에서도 'aa' 모두 포함해야 함.

        슬라이딩 윈도우 활용!
        최초 길이는 t의 길이 만큼
        내부적으로 윈도우가 포함하고 있는 글자 종류 및 개수 추적

        t 내부 문자열 정리 -> ~N
        s를 윈도우로 탐색 -> ~M
        -> ~(M + N)
        """

        # s가 t보다 짧은 경우는 항상 "" 반환
        if len(s) < len(t):
            return ""
        
        if s == t:
            return t

        # t 문자열을 dict로 정리 (Counter 활용도 가능)
        target = defaultdict(int)
        for char in t:
            target[char] += 1
        # print(target)
        # print()

        # 윈도우 초기화
        window = defaultdict(int)
        left, right = 0, 0
        window[s[0]] += 1
        
        # 윈도우 진행하기
        min_string = s + t
        while True:
            # 종료 조건 윈도우가 문자열을 전부 탐색했을 때
            if right >= len(s) - 1 and left > right:
                break

            # print(s[left:right + 1], window)

            # 정답 조건에 포함될 경우 힙에 추가
            if self.is_window_string(window, target):
                if right - left + 1 < len(min_string):
                    min_string = string = s[left:right + 1]

                # print(string)
                
                window[s[left]] -= 1
                left += 1
                continue
            
            # 정답 조건이 아니면 윈도우 이동
            if right < len(s) - 1:
                right += 1
                window[s[right]] += 1
            else:
                window[s[left]] -= 1
                left += 1
                

        if len(min_string) == len(s) + len(t):
            return ""
        return min_string


    def is_window_string(self, window, target):
        for key in target.keys():
            if window[key] < target[key]:
                return False

        return True