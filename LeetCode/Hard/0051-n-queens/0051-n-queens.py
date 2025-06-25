class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []

        def is_safe(stack, row, col):
            # stack[i]는 i번째 row의 queen이 위치한 column
            for r, c in enumerate(stack):
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        def backtracking(row, stack):
            if row == n:
                # 모든 row에 다 놓았으므로 결과 저장
                board = []
                for c in stack:
                    line = ['.'] * n
                    line[c] = 'Q'
                    board.append(''.join(line))
                answer.append(board)
                return
                
            for col in range(n):
                if is_safe(stack, row, col):
                    stack.append(col)
                    backtracking(row + 1, stack)
                    stack.pop()

        backtracking(0, [])
        return answer

