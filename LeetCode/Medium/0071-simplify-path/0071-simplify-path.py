class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        # 스택 활용

        # .은 그대로
        # ..이면 pop
        # ...은 파일이름이거나 디렉토리 이름
        # /이 있는 상태에서 /가 나오면 패스
        # / 만 있는 게 아닌 상태에서 /로 끝나면 pop

        stack = ['']
        for p in path:
            if p == '.' or p == '':
                continue

            if p == '..':
                if len(stack) > 1:
                    stack.pop()
            else: stack.append(p)
        
        # if len(stack) > 1 and stack[-1] == '/':
        #     stack.pop()
        if len(stack) == 1:
            return '/'
        return '/'.join(stack)
            