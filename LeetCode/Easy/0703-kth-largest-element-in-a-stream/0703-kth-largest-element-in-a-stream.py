import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.target = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # min heap 기준으로 길이가 k가 되도록 유지하면 됨
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.target:
            heapq.heappop(self.heap)
        
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)