from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # k 크기의 윈도우가 왼쪽에서 오른쪽 끝으로 이동
        # 이때 각 움직임마다의 최댓값을 리스트로 모아 반환

        window = deque()
        # 최초 윈도우 초기화
        for i in range(k):
            # 덱을 내림차순으로 유지되도록 pop하고 추가
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)

        answer = [nums[window[0]]]
        # 윈도우 이동하며 결과 추가하기
        for i in range(k, len(nums)):
            # 현재 왼도우 왼쪽이 윈도우를 벗어나면 pop
            if window[0] < i - k + 1:
                window.popleft()

            # 덱을 내림차순으로 유지되도록 pop하고 추가
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
            answer.append(nums[window[0]])
        
        return answer
                