class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        리스트에 없는 양의 정수 최솟값 찾기
        
        제약:
        공간 복잡도 ~1
        시간 복잡도 ~N

        리스트를 한 번만 순회하고, 추가 공간 사용을 포인터 선에서 끝내야 제약 조건 만족        
        
        Swap 방식
        리스트 인덱스 위치에 (인덱스 + 1) 값이 오도록 swap하기
        
        루프 조건
        리스트 각 요소에 대해 해당 위치에 적절한 값이 담길 떄까지 Swap 루프 진행

        """
        # it = 0
        for i in range(len(nums)):
            while True:
                # 현재 리스트 값이 양의 정수가 아니거나 리스트 값을 벗어나면 Swap 안함
                if 1 > nums[i] or nums[i] > len(nums):
                    break
                # print("인덱스: ", i)
                # print("변경 전 ",nums)
                # print(nums[i])
                # 현재 리스트 인덱스 위치에 있는 값이
                # (인덱스 + 1)에 해당하는 값이 아니면
                # 현재 값을 적절한 위치로 Swap 해줌.

                
                if nums[nums[i] - 1] != nums[i]:
                    temp = nums[nums[i] - 1] 
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = temp
                else: break
                # if it > 3:
                #     break
                # it += 1
                
        
        return self.find_missing_positive(nums)
        
    def find_missing_positive(self, nums):
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1