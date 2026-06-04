class MinStack:

    """
    1,4,3,2

    [(1,1), (4, 1), (3, 1), (2,1)]

    4,3,5,2,1
    [(4,4), (3,3), (5,3), (2,2), (1,1)]

    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
