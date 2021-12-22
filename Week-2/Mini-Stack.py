class MinStack:

    def __init__(self):
        self.obj = []
        

    def push(self, val: int) -> None:
        self.obj.append(val)
        

    def pop(self) -> None:
        self.obj.pop()

    def top(self) -> int:
        return self.obj[len(self.obj)-1]

    def getMin(self) -> int:
        return min(self.obj)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
