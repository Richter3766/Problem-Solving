import heapq
from collections import defaultdict
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 빌딩 윤곽 구하기
        # 빌딩 덩어리에서 사람이 멀리서 봤을 때 보이는 윤곽점을 찾는 것
        # 단 빌딩 덩어리를 나타내는 마지막 요소의 y는 항상 0

        # 항상 높이가 최대인 지점이 윤곽이 됨
        # 최대 힙 활용
        # 최대 높이를 관리하며 이전 높이보다 높아지면 윤곽을 찍는다
        # 힙이 비어지면 마지막 윤곽으로 y가 0이 됨
        event = []

        for left, right, height in buildings:
            event.append((left, -height)) # 같은 시작점이면 높은 height가 먼저 오도록 하기 위함
            event.append((right, height)) # 시작점과 구분하기 위함
            
        event.sort(key=lambda x: (x[0], x[1])) # x 기준으로 정렬

        answer = []
        heap = []
        prev = 0
        counter = defaultdict(int)
        for x, height in event:
            # h가 음수면 건물 시작이므로 heap에 push
            if height < 0:
                heapq.heappush(heap, height)
                counter[height] += 1 # lazy removal을 위한 카운터
            # 양수면 건물 끝이므로 pop
            else:
                counter[-height] -= 1

            while heap and counter[heap[0]] == 0:
                heapq.heappop(heap)
            
            # 최대 높이 바뀌었으면 윤곽 추가
            # 만약 HEAP이 비어있다면 Y를 0으로
            if not heap:
                answer.append((x, 0))
                prev = 0
            elif heap[0] != prev:
                answer.append((x, -heap[0]))
                prev = heap[0]

        return answer
                    
                    
