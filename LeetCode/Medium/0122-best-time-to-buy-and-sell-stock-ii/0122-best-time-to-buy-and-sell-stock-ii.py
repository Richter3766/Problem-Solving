class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp 문제
        주식은 한 번에 하나만 보유 가능: 언제 주식을 구매했는 지 알 필요 없이 보유 여부만 고민하면 됨.
        dp[i][0] : i번째 날에 주식을 보유하지 않은 경우 최대 이익
        dp[i][1] : i번째 날에 주식을 보유한 경우 최대 이익

        당일 기준 최대 이익 구하기
        - dp[i][0]:
            1. 어제 미보유 상태, 오늘도 미보유 상태: dp[i - 1][0]
            2. 어제 보유 상태, 오늘 미보유 상태(차익 실현): dp[i - 1][1] + prices[i]
        
        - dp[i][1]:
            1. 어제 미보유 상태, 오늘 보유 상태(주식 구매): dp[i - 1][0] - prices[i]
            2. 어제 보유 상태, 오늘 보유 상태: dp[i - 1][1]
        
        두 부분 다 1, 2 중 max를 저장하도록 함.
        정답의 경우 마지막 날 주식을 미보유한 상태임.(모든 주식을 판 상태여야 최대 일 것)
        """
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0] # 첫날 주식을 산 경우
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

