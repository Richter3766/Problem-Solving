class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        보드에서 단어 찾기
        백트래킹으로 우선 풀어보고,
        더 좋은 방식이 있는지 찾아보기

        visited 리스트 하나만 활용해서 써보자
        """

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        def backtracking(row, col, idx):
            if idx == len(word):
                return True

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and not visited[nr][nc]:
                    if board[nr][nc] == word[idx]:
                        visited[nr][nc] = True
                        is_found = backtracking(nr, nc, idx + 1)
                        if is_found: return True
                        visited[nr][nc] = False

            return False
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visited[r][c] = True
                    is_found = backtracking(r, c, 1)
                    if is_found: return True
                    visited[r][c] = False
    
        return False