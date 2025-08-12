from collections import deque

class MyStack:
    # 두 개의 큐로 스택을 구현할 때에는
    # 항상 두 큐를 스왑하는 과정이 필요하다.
    # pop, push 두 연산 중 하나는 항상 O(N)
    def __init__(self):
        self.head = deque()
        self.tail = deque()

    def push(self, x: int) -> None:
        self.head.append(x)
        self.head.extend(self.tail)
        self.tail = self.head
        self.head = deque()

    def pop(self) -> int:
        return self.tail.popleft()

    def top(self) -> int:
        return self.tail[0]

    def empty(self) -> bool:
        return not self.head and not self.tail
            


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()