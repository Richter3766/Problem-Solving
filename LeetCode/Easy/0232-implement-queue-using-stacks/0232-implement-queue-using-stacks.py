class MyQueue:

    def __init__(self):
        self.front = []
        self.tail = []
        
    def push(self, x: int) -> None:
        self.tail.append(x)

    def pop(self) -> int:
        if self.front:
            return self.front.pop()
        while self.tail:
            self.front.append(self.tail.pop())

        return self.front.pop()

    def peek(self) -> int:
        if self.front:
            return self.front[-1]
        return self.tail[0]

    def empty(self) -> bool:
        return not self.front and not self.tail


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()