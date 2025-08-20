class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # 모든 정점에서 다른 정점으로 이동할 때
        # 거리 제한 내에 있는 정점수가 가장 적은 도시 찾기
        # 모든 정점에서 다른 정점으로의 경로의 최소가 필요하므로
        # 플로이드 워셜을 적용
        INF = float('inf')
        graph = [[INF for _ in range(n)] for _ in range(n)]
        
        # 그래프 초기 상태 만들기
        for start, end, weight in edges:
            graph[start][end] = weight
            graph[end][start] = weight
        
        for k in range(n):
            for s in range(n):
                for e in range(n):
                    if graph[s][k] != INF and graph[k][e] != INF:
                        graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

        answer = None
        prev_cities = INF
        for i in range(n):
            cur_cities = sum(1 for j in range(n) if i != j and graph[i][j] <= distanceThreshold)
            if cur_cities <= prev_cities:
                answer = i
                prev_cities = cur_cities
        
        return answer