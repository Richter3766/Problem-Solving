class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        문자열 매칭 문제
        '?'은 단일 문자 무조건 매칭
        '*'은 문자열 무조건 매칭
        '*'의 경우 '*' 이후에 나오는 문자열이 있다면 해당 패턴도 매칭되는 지 잘 봐야 함.

        모든 가능성을 탐색해야 하고,
        이전의 결과가 재사용되어야 하는 상황임.
        -> DP 선택

        행에 p, 열에 s를 각각 매칭
        dp[i][j]: p[i:] == s[j:]
        """
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[len(p)][len(s)] = True   # 역순으로 탐색하므로 마지막은 True로 둚.
        
        for i in range(len(p)-1, -1, -1):
            if p[i] == '*':
                dp[i][len(s)] = dp[i+1][len(s)]
            else:
                dp[i][len(s)] = False

        for i in range(len(p)-1, -1, -1):
            for j in range(len(s)-1, -1, -1):
                if p[i] == '*':
                    dp[i][j] = dp[i + 1][j] or dp[i][j + 1]
                elif p[i] == '?' or p[i] == s[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = False
        return dp[0][0]