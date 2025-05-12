class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        두 개의 정렬된 리스트가 주어질 때
        미디안 값 찾기
        """
        if len(nums1) <= len(nums2):
            return self.find_median(nums1, nums2)
        else: return self.find_median(nums2, nums1)

    def find_median(self, nums1: List[int], nums2: List[int]):
        total_count = (len(nums1) + len(nums2) + 1) // 2
        left, right = 0, len(nums1)

        while True:
            nums1_mid = (left + right) // 2
            nums2_mid = total_count - nums1_mid

            max_left_nums1 = self.get_max_left(nums1, nums1_mid)
            min_right_nums1 = self.get_min_right(nums1, nums1_mid)

            max_left_nums2 = self.get_max_left(nums2, nums2_mid)
            min_right_nums2 = self.get_min_right(nums2, nums2_mid)
            
            if max_left_nums1 > min_right_nums2:
                right = nums1_mid - 1
            elif max_left_nums2 > min_right_nums1:
                left = nums1_mid + 1
            else:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(max_left_nums1, max_left_nums2)
                else:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2

    def get_max_left(self, arr, i):
        return arr[i - 1] if i > 0 else float('-inf')

    def get_min_right(self, arr, i):
        return arr[i] if i < len(arr) else float('inf')        
            
