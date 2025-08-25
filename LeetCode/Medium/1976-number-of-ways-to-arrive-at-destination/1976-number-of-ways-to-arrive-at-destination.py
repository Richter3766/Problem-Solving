import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # 0에서 n - 1 지점까지 가는 최소 경로의 갯수 구하기
        # 양방향 경로임, 항상 양의 가중치
        
        # 다익스트라로 최단 경로 값을 구하며,
        # 계속해서 경로 수를 카운팅해주기
        # 힙으로 순서를 관리하므로 최단 경로가 확정적이기 때문
        graph = self.build_graph(roads)

        heap = [(0, 0)]
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0], ways[0] = 0, 1
        MOD = (10 ** 9) + 7
        while heap:
            weight, cur = heapq.heappop(heap)

            if dist[cur] < weight: continue

            for e, w in graph[cur]:
                new_weight = w + weight

                if new_weight < dist[e]:
                    dist[e] = new_weight
                    ways[e] = ways[cur]
                    heapq.heappush(heap, (new_weight, e))
                elif new_weight == dist[e]:
                    ways[e] += ways[cur]

        return ways[-1] % MOD


    def build_graph(self, roads):
        graph = defaultdict(list)

        for start, end, time in roads:
            graph[start].append((end, time))
            graph[end].append((start, time))
        
        return graph