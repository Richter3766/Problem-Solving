import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        uglys = []
        visited = {}
        while True:
            if len(uglys) == n:
                return uglys[-1]
            
            cur = heapq.heappop(heap)
            uglys.append(cur)
            for factor in [2, 3, 5]:
                new = cur * factor
                if new not in visited:
                    visited[new] = True
                    heapq.heappush(heap, cur * factor)
