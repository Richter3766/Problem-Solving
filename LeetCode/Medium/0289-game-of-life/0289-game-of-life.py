from itertools import product

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 보드판
        # 1: 살아있음
        # 0: 죽음
        
        # 규칙
        # 1. 자기 주변 8칸 이내에 1이 2 미만이면 죽음
        # 2. 2~3개 1이면 그대로 살아감
        # 3. 4 이상이면 죽음
        # 4. 정확히 3개의 1이 있으면 0이 1이 됨

        # 현재 상태에서 한번 위 규칙을 진행했을 때의 상태 만들기
        # 변화는 동시에 일어나므로 순차적으로 계산하되
        # 임시 상태를 저장해둘 공간이 필요함
        eboard = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        
        def count_neighbors(r, c):
            directions = product([-1, 0, 1], repeat=2)
            
            count = 0
            for dr, dc in directions:
                if dr == dc == 0: continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    count += board[nr][nc]
            
            return count

        for r in range(len(board)):
            for c in range(len(board[0])):
                count = count_neighbors(r, c)
                if count < 2: eboard[r][c] = 0
                elif count > 3: eboard[r][c] = 0
                elif count == 3: eboard[r][c] = 1
                else: eboard[r][c] = board[r][c]

        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = eboard[r][c]