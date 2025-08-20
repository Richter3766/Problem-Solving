class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 이진 탐색 응용
        # 이진 탐색으로 최초 위치 찾기
        # 좌우 경계를 각각 찾는다

        def lower_bound(a: List[int], x: int) -> int:
            left, right = 0, len(a)  # [left, right)
            while left < right:
                mid = (left + right) // 2
                if a[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            return left  # first index with a[i] >= x

        def upper_bound(a: List[int], x: int) -> int:
            left, right = 0, len(a)  # [left, right)
            while left < right:
                mid = (left + right) // 2
                if a[mid] > x:
                    right = mid
                else:
                    left = mid + 1
            return left  # first index with a[i] > x

        l = lower_bound(nums, target)
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        r = upper_bound(nums, target) - 1
        return [l, r]