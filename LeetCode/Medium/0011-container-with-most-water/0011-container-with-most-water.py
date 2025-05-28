class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 최대 넓이가 궁금하므로 투 포인터를 활용하자.
        left, right = 0, len(height) - 1
        max_area = 0

        while left <= right:                
            # 현재 포인터 위치에서의 넓이 계산 후 최댓값 갱신
            cur_size = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, cur_size)

            if height[left] > height[right]:
                right -= 1
            else: left += 1
        return max_area
    