import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # heap으로 k개의 최대 원소만 관리
        # 모든 nums 원소를 순회했을 때 heap의 top이 정답
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
                continue
            
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]
