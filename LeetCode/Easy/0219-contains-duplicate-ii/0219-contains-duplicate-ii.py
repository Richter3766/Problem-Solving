class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 수 배열에서 어떤 인덱스 i, j에 대해
        # nums[i] == nums[j]이고
        # abs(i - j) <= k를 만족하는
        # i, j 가 존재하면 true 아니면 False

        num_set = set()

        for num in nums[:k + 1]:
            if num in num_set:
                return True
            num_set.add(num)
        
        for i in range(k + 1, len(nums)):
            num_set.remove(nums[i - k - 1])
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])

        return False
        