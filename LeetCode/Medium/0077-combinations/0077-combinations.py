import copy

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        n, k가 주어질 때
        range(1, n)까지에 대한 수에 대해 k개를 뽑는 조합 모두 구하기
        mCk

        combinations 라이브러리를 활용하면 바로 풀리겠지만,
        사용하지 않고 해결해보기

        모든 조합을 구하려면 백트래킹 활용이 가장 무난할 듯
        이전 값보다 항상 큰 값을 선택해서 반복하도록 하기
        """

        answer = []
        def backtracking(comb, value):
            if len(comb) == k:
                answer.append(copy.deepcopy(comb))
                return
            
            for i in range(value, n + 1):
                comb.append(i)
                backtracking(comb, i + 1)
                comb.pop()

        backtracking([], 1)

        return answer
            