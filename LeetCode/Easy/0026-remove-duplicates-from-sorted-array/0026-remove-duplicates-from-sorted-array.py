class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        left, right = 0, 1
        while True:
            if right >= len(nums): break
            
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]

        return left + 1
        