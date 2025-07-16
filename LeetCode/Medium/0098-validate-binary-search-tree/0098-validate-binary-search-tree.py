# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        주어진 트리가 적절한 BST인지 검증하기

        재귀적으로 트리를 순회하며 아래 동작을 하면 됨.
        1. 루트에서 시작
        2. 왼쪽 노드가 루트보다 작은 지 확인
        3. 오른쪽 노드가 루트보다 큰 지 확인
        4. 다음 노드로 재귀 탐색

        중간에 하나라도 False가 반환되면 전체가 False가 되도록 반환

        탐색 시 왼쪽 노드인데, 상위 노드의 값보다 크거나,
        오른쪽 노드인데, 상위 노드의 값보다 작은 경우가 있어도 False 반환
        """
        
        def validate(cur, low, high):
            if cur is None:
                return True

            if not (low < cur.val < high):
                return False

            return (validate(cur.left, low, cur.val) 
                    and
                    validate(cur.right, cur.val, high))
            

        return validate(root, float('-inf'), float('inf'))
