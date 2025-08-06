import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n개의 노드, 1~n까지 라벨링
        # times 리스트 -> (u, v, w) 
        # u -> v 방향, w 걸리는 시간

        # 주어진 노드 k에서 보낼 때 모든 n에 받는 시간의 최소 값
        # 불가능하면 -1 리턴
        # 다익스트라로 구현

        # 인접 리스트로 그래프 생성
        # def build_graph():
        #     graph = [[float('inf') for _ in range(n)] for _ in range(n)]

        #     for start, end, weight in times:
        #         graph[start][end] = weight
        #     return graph 

        def build_graph():
            graph = defaultdict(list)
            for start, end, weight in times:
                graph[start - 1].append((weight, end - 1))
            return graph

        graph = build_graph()
        def find_shortest_path():
            weights = [float('inf') for _ in range(n)]
            weights[k - 1] = 0
            heap = [(0, k - 1)]

            while heap:
                weight, cur = heapq.heappop(heap)

                if weight > weights[cur]: continue

                for w, end in graph[cur]:
                    new_weight = weight + w

                    if new_weight < weights[end]:
                        weights[end] = new_weight
                        heapq.heappush(heap, (new_weight, end))

            return weights
        
        weights = find_shortest_path()

        return max(weights) if float('inf') not in weights else -1


