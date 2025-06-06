# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # n 개의 정렬된 링크드 리스트를 하나의 링크드 리스트로 만들기
        # 기본 개념은 2개 리스트를 합칠 때와 같음
        # 근데 n개 이므로 병합할 때마다 n번 탐색 과정 필요
        # 그럴거면 힙을 쓰는 게 나을지도

        """
        의사 코드
        # 주어진 리스트의 첫 값을 최소 힙에 푸쉬하기
        
        # 최소힙에서 heappop으로 꺼내어 현재 리스트에 연결
        # 꺼낸 리스트의 다음 값을 힙에 푸쉬하기
        # 끝날 때까지 위 행동 반복
        """
        head = ListNode()
        cur = head
        heap = []
        for i, llist in enumerate(lists):
            if llist is not None:
                heapq.heappush(heap, (llist.val, i, llist))
    
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))
            cur = node
        return head.next