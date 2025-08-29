class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 왼쪽 누적곱 구하기
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer