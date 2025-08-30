import heapq

class MedianFinder:

    def __init__(self):
        self.left = []  # 중간값 기준 작은 값을 담을 힙 -> max heap
        self.right = [] # 중간값 기준 큰 값을 담을 힙 -> min heap

    def addNum(self, num: int) -> None:
        # 핵심은 두 힙의 길이가 같도록 유지하는 것
        # 그리고 왼쪽 힙의 탑은 오른쪽 힙의 탑보다 항상 작아야 함
        # num이 왼쪽 힙 탑보다 작다면 바로 push
        # 큰 경우 오른쪽 힙 탑보다 작은지 확인하고 push
        # 오른쪽 힙 탑보다 큰 경우?
        # 오른쪽 pop해서 왼쪽에 넣고, num 오른쪽에 push
        heapq.heappush(self.left, -num)

        # 정렬 불변식 보장: left의 최대(= -left[0])를 right로 넘겨
        #    left의 모든 값 <= right의 모든 값이 되게 한다.
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # 크기 불변식 보장: left가 항상 right보다 같거나 1개 더 많도록
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))


        # if not self.left:
        #     heapq.heappush(self.left, -num)
        # elif -self.left[0] < num:
        #     heapq.heappush(self.right, num)
        # else:
        #     heapq.heappush(self.left, -num)

        # # 길이 균형이 깨지면 길이가 큰 쪽에서 pop하여 작은쪽에 push
        # if abs(len(self.left) - len(self.right)) >= 2:
        #     if len(self.left) > len(self.right):
        #         cur = heapq.heappop(self.left)
        #         heapq.heappush(self.right, -cur)
        #     else:
        #         cur = heapq.heappop(self.right)
        #         heapq.heappush(self.left, -cur)
        # print(self.left, self.right)

    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)
        if total % 2 == 1:
            # 홀수면 left가 하나 더 많음
            return float(-self.left[0])
        else:
            # 짝수면 양쪽 top 평균
            return (-self.left[0] + self.right[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()