# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        BST는 중위 순회 시 오름차순으로 값을 읽게 된다.
        만약 순회 중 오름차순이 아닌 곳이 나오면 그곳이 노드가 스왑되어 있다는 뜻
        확장성을 고려해 두 개 이상의 노드가 스왑되어 있어도 문제가 풀리도록 해보자
        """
        node_list = []
        val_list = []

        def inorder(node):
            if not node: return # None이면 넘어가기

            inorder(node.left)
            # 노드 포인터와 값을 각각 저장
            node_list.append(node)
            val_list.append(node.val)
            inorder(node.right)
        
        inorder(root)

        # 정렬
        val_list.sort()

        # 값을 읽으며 트리 다시 만들기
        for i, val in enumerate(val_list):
            node_list[i].val = val
        