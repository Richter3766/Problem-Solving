class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
            가장 긴 완성된 괄호 찾기
            
            스택은 [-1]로 초기화
            1. '('가 나오면 스택에 현재 인덱스 넣기
            2. ')'가 나오면 
            - 스택에서 pop 하기
            - 만약 스택이 비었으면 현재 인덱스 넣고 넘어가기
            - 아니면 최대 길이 갱신하기 -> max(max_len, cur_idx - stack[-1])
        """
        max_len = 0      # 최대 괄호 길이
        stack = [-1]      # '('를 담아둘 스택
        for i in range(len(s)):
            # '('인 경우
            if s[i] == '(':
                stack.append(i)
                continue
            
            # 2. ')'가 나오면 
            # - 스택에서 pop 하기
            stack.pop()
            # - 만약 스택이 비었으면 현재 인덱스 넣고 넘어가기
            if len(stack) == 0:
                stack.append(i)
                continue
            # - -1이 아니면 최대 길이 갱신하기 -> max(max_len, cur_idx - stack[-1])
            max_len = max(max_len, i - stack[-1])

        return max_len