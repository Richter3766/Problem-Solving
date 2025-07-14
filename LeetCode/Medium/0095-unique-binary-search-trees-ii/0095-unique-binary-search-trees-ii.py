# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        모든 BST 구조 생성 문제

        1. 트리이므로 분할 정복과 재귀를 활용하는 것이 자연스러움
        2. BST이므로 트리 val 값에 따라 범위가 나뉨
        """
        def generate(left, right):
            result = []
            if left > right:
                return [None]
            
            for i in range(left, right + 1):
                # i 를 루트로 잡았을 때 가능한 모든 좌우 서브트리 조합을 생성
                left_subtrees = generate(left, i - 1)
                right_subtrees = generate(i + 1, right)

                # 각 좌우 트리에 대해 가능한 모든 트리 조합 생성
                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root = TreeNode(i)
                        root.left = left_subtree
                        root.right = right_subtree
                        result.append(root)

            return result

        answer = generate(1, n)
        
        return answer
