class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 서로 다른 인덱스에 있는 값의 합이 0이 되는  triple을 찾아 반환하기
        answer = set()
        # 리스트를 정렬하고,
        # 한 점 고정 후 투 포인터 활용
        nums.sort() # NlogN
        for pin in range(len(nums) - 2): # 겹치면 안되는 규칙이 있음.
            left, right = pin + 1, len(nums) - 1
            pin_num = nums[pin]
            if pin_num > 0: break 
            while left < right:
                cur_sum = pin_num + nums[left] + nums[right]
                if cur_sum == 0:
                    answer.add((nums[pin], nums[left], nums[right]))
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else: right -= 1

        return list(answer)


