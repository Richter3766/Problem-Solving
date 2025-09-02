class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []

        for interval in intervals:
            if not answer:
                answer.append(interval)
                continue
            
            if answer[-1][1] >= interval[0]:
                answer[-1][1] = max(answer[-1][1], interval[1])
            else: answer.append(interval)
        
        return answer