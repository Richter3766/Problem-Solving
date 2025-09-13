class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            r, c = divmod(mid, n)  # r = mid // n, c = mid % n
            val = matrix[r][c]

            if val == target:
                return True
            if val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False