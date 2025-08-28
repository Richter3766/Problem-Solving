class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 글자 별로 문자열에서 등장하는 마지막 위치를 계산
        last_index = {}

        for i in range(len(s)):
            last_index[s[i]] = i
        
        # 문자열을 다시 훑으면서 현재 문자가 이전문자보다 사전순으로 빠를 때
        stack = []
        visited = set()
        for i, char in enumerate(s):
            if char in visited:
                continue

            # 이전 문자가 이후에도 나오는 문자라면
            # 해당 문자를 pop    
            # 위를 첫 두줄 조건에 만족하지 않을 때까지 반복
            while stack and char < stack[-1] and last_index[stack[-1]] > i:
                popped = stack.pop()
                visited.remove(popped)

            # 현재 글자 push
            stack.append(char)
            visited.add(char)

        answer = ''.join(stack)
        return answer

        
        
