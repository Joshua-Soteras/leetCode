class MinStack:

    def __init__(self):
        self.minStackTracker = []
        self.stack = []

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        
        
        if not self.minStackTracker or (self.minStackTracker[-1] >= val): 
            self.minStackTracker.append(val)
        

    def pop(self) -> None:

        if self.minStackTracker[-1] == self.stack[-1]:
            self.minStackTracker.pop()
        
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStackTracker[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
