class Solution:
    def totalNQueens(self, n: int) -> int:
        # 퀸을 놓을 수 있는 지 검사하는 함수
        def is_safe(row, col, stack):
            for r, c in enumerate(stack):
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        # 백트래킹 함수
        def backtracking(row, stack, answer):
            # 종료 조건인지 검사, if len(stack) == n
            if len(stack) == n:
                return answer + 1

            # 그 다음 퀸 위치 탐색
            for col in range(n):
                if is_safe(row, col, stack):
                    stack.append(col)
                    answer = backtracking(row + 1, stack, answer)
                    stack.pop()

            return answer
        # 백트래킹 시작
        answer = backtracking(0, [], 0)
        return answer
        
