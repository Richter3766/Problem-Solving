class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 양수로 이루어진 nums와 target,
        # nums의 subarray의 합이 target보다 크거나 같도록 하는
        # subarray의 최소 길이
        # 만약 없다면 0 반환

        # subarray이므로 슬라이딩 윈도우 생각 가능
        # 구간이 정해져 있고, 내부 값을 추적해야 하기 때문

        # 가변 길이의 윈도우
        # 윈도우 내 값이 target보다 작으면 확장하고
        # target보다 커지면 정답을 갱신한 후 값을 줄여볼 수 있음
        left = 0
        window_sum = 0
        answer = float('inf')
        for right, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                answer = min(answer, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        return answer if answer != float('inf') else 0