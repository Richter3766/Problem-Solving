# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder는 루트 (왼쪽) (오른쪽) 순
        # inorder는 (왼쪽) 루트 (오른쪽) 순
        # preorder에서 root를 찾고 이를 기준으로 
        # inorder에서 왼쪽, 오른쪽 서브 트리를 나누어 탐색한다.

        # 빠른 인덱스 탐색을 위한 인덱스 만들기
        cache = {}
        for i, val in enumerate(inorder):
            cache[val] = i

        def build(pre_left, pre_right, in_left, in_right):
            if pre_left >= pre_right or in_left >= in_right:
                return None

            root = TreeNode(preorder[pre_left])
            idx = cache[root.val]
            left_size = idx - in_left
                
            root.left= build(pre_left + 1, pre_left + 1 + left_size, in_left, idx)
            root.right = build(pre_left + 1 + left_size, pre_right, idx + 1, in_right)

            return root

        return build(0, len(preorder), 0, len(inorder))