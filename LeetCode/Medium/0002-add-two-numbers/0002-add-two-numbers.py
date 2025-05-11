# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = self.make_num(l1) + self.make_num(l2)
        return self.num_to_list(num)
    
    def make_num(self, node: Optional[ListNode]):
        num = 0
        digit = 1
        cur = node
        while cur:
            num += digit * cur.val
            digit *= 10
            cur = cur.next

        return num

    def num_to_list(self, num: int) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        cur_digit = num
        while True:
            cur_digit, remainder = divmod(cur_digit, 10)
            cur.val = remainder
            if cur_digit == 0: break
            
            cur.next = ListNode()
            cur = cur.next
            

        
        return head