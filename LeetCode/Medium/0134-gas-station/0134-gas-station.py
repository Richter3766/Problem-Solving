class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        # 그리디 문제
        # 어떤 시작점에서 인덱스 i까지 진행했을 때
        # 값이 음수가 되면 그 시작점에서 i까지는 항상 정답이 될 수 없음
        # start = i + 1부터 다시 시작
        total_tank = 0    # 전체 합
        curr_tank = 0     # 현재 구간 연료
        start_index = 0   # 후보 시작점

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff

            # 현재 구간 실패 → i 다음부터 새로 시작
            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        # 전체 합이 음수면 불가능
        return start_index if total_tank >= 0 else -1

        
        


