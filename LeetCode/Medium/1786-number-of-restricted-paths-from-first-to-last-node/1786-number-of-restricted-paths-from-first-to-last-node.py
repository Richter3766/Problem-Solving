import heapq
from collections import defaultdict

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # 무방향 가중치 그래프
        # n개의 노드, 1 ~ n
        # 경로의 길이는 경로 가중치 합
        # 1부터 n까지 이동하는 엄격한 경로 구하기
        # 엄격한 경로란 이동할 때 반드시 최단경로 값이 감소해야함을 의미

        # 항상 n이 도착점이므로 n에서 다익스트라 사용
        # 그럼 어떤 지점 x 에서 n까지 가는 최솟값도 나온다(무방향이므로)
        # 이후 n를 출발지로 항상 내림차순이 되도록 가능한 경로 수를 카운팅
        # 출발지가 1인 곳에서의 경로 수를 반환하면 정답

        # 그래프 만들기
        def build_graph():
            graph = defaultdict(list)

            for start, end, weight in edges:
                graph[start - 1].append((end - 1, weight))
                graph[end - 1].append((start - 1, weight))
            
            return graph
        graph = build_graph()

        # 다익스트라로 n을 시작점으로 한 최단 경로 구하기
        def find_shortest_path():
            weights = [float('inf') for _ in range(n)]
            weights[-1] = 0

            heap = [(0, n - 1)]
            while heap:
                weight, cur = heapq.heappop(heap)

                if weight > weights[cur]:
                    continue

                for e, w in graph[cur]:
                    new_weight = w + weight
                    if new_weight < weights[e]:
                        weights[e] = new_weight
                        heapq.heappush(heap, (new_weight, e))
            
            return weights
        weights = find_shortest_path()
        
        MOD = (10 ** 9) + 7
        print(MOD)
        memo = [-1] * n
        def dfs(u):
            if u == n - 1: return 1
            if memo[u] != -1: return memo[u]

            total = 0
            for (v, w) in graph[u]:
                if weights[v] < weights[u]:
                    total += dfs(v)
            
            memo[u] = total
            return total
        answer = dfs(0)

        return answer % MOD
            
        
