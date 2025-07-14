class Solution:
    def numTrees(self, n: int) -> int:
        """
        이전과 똑같은 문제, 대신 갯수 세기
        똑같이 풀고 정답을 len으로 넘겨주면 끝
        """
        cache = {}
        def generate_trees(left, right):
            result = 0
            
            if left > right:
                return 1

            if (left, right) in cache:
                return cache[(left, right)]

            for i in range(left, right + 1):
                left_subtrees = generate_trees(left, i - 1)
                right_subtrees = generate_trees(i + 1, right)

                result += left_subtrees * right_subtrees
            cache[(left, right)] = result
            return result

        answer = generate_trees(1, n)
        return answer