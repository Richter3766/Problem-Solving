import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        power set 만들기

        백트래킹으로 충분히 구현 가능
        """

        answer = []

        def backtracking(cur, idx):
            answer.append(copy.copy(cur))
            if len(cur) == len(nums):
                return

            for i in range(idx, len(nums)):
                num = nums[i]
                cur.append(num)
                backtracking(cur, i + 1)
                cur.pop()

        backtracking([], 0)

        return answer