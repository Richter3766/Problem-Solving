# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_head = list1
        list2_head = list2
        head = ListNode()
        cur = head
        
        while True:
            if list1_head is None or list2_head is None:
                break
            if list1_head.val > list2_head.val:
                cur.next = self.create_node(list2_head.val)
                list2_head = list2_head.next
            else: 
                cur.next = self.create_node(list1_head.val)
                list1_head = list1_head.next
            cur = cur.next

        if list1_head is None:
            cur.next = list2_head
        else:
            cur.next = list1_head

        return head.next

    def create_node(self, val, next=None):
        return ListNode(val=val)