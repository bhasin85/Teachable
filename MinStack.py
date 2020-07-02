class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] # (value, min_value)
        

    def push(self, x: int) -> None:
        _min = min(x, self.getMin())
        self.stack.append((x, _min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return float("inf") if len(self.stack) == 0 else self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
