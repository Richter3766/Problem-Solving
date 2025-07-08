# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        주어진 x보다 작은 값은 x 왼쪽,
        크거나 값은 값은 그대로 두기

        리스트를 순회하며 처음으로 만나는 x보다 크거나 값은 값을 중심으로 잡기
        이후 만나는 모든 x보다 작은 값을 해당 위치로 이동하기
        -> 포인터가 많아 복잡하고 가독성이 떨어짐

        두 스택 포인터를 관리 
        -> less_head, greater_head
        기준 x보다 작은 값은 less_head에 이어붙이기
        기준 x보다 크거나 같은 값은 greater_head에 이어붙이기
        
        """
        cur = head
        less_head = less_tail = ListNode()
        greater_head = greater_tail = ListNode()

        while cur: # 모든 리스트 값 순회
            if cur.val < x:
                less_tail.next = cur
                less_tail = cur
            else:
                greater_tail.next = cur
                greater_tail = cur
        
            cur = cur.next
        
        less_tail.next = greater_head.next
        greater_tail.next = None

        return less_head.next
        
