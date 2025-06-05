class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 주어진 수만큼 완성된 괄호 쌍을 모두 만들기
        # 바로 떠오르는 건 백트래킹

        """
        # 백트래킹 의사 코드
        여는 괄호 수 == 닫는 괄호 수 == n: 
            결과에 추가
            후 리턴

        if 여는 괄호 수가 n보다 작을 때:
            여는 괄호 추가
            백트래킹
            여는 괄호 제거
        
        if 닫는 괄호 수가 여는 괄호 수보다 작을 때:
            닫는 괄호 추가
            백트래킹
            닫는 괄호 제거
        """
        answer = []
        cur = ''
        
        self.backtracking(n, answer, cur, 0, 0)

        return answer
    
    def backtracking(self, n: int, answer: list, cur: str, open_num: int, close_num:int):
        if open_num == close_num == n:
            answer.append(cur)
            return
        
        if open_num < n:
            cur += '('
            self.backtracking(n, answer, cur, open_num + 1, close_num)
            cur = cur[:-1]

        if close_num < open_num:
            cur += ')'
            self.backtracking(n, answer, cur, open_num, close_num + 1)
            cur = cur[:-1]
