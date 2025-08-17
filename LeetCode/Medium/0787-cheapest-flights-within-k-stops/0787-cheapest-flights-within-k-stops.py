import copy

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # k개 경유지를 가질 때
        # src에서 dst까지의 최소 cost 구하기
        # 시작점과 끝점이 명확하므로 다익스트라 방식이 유효해 보이지만
        # k개의 경유지가 한계로 주어짐을 생각해야 함
        # 플로이드 워셜의 변형판을 써볼까
        INF = float('inf')        

        dp = [INF] * n
        dp[src] = 0

        for t in range(k + 1):
            prev = copy.copy(dp)

            for start, end, cost in flights:
                if prev[start] == INF:
                    continue
                dp[end] = min(dp[end], prev[start] + cost)
        
        return dp[dst] if dp[dst] != INF else -1


