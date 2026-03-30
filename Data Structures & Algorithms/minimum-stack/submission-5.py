class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(len(self.minStack) if not self.minStack or val < self.stack[self.minStack[-1]] else self.minStack[-1])

    def pop(self) -> None:
        while self.minStack and self.minStack[-1] == len(self.stack)-1:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minStack[-1]]