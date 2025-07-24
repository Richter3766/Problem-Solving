class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        이미 정렬된 두 배열을 합쳐
        하나의 정렬된 배열로 만들기

        포인터를 하나씩 옮기면 될듯
        앞에서부터 채울 경우 덮어씌워지므로
        뒤에서부터 채워넣기
        """
        # 각 배열의 마지막 포인터들 
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # nums2에 남은 값이 있을 때만 복사
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]
