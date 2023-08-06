# get_min complexity O(1)
class MinStack:
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
        if self.stack != []:
            return self.stack[-1]
        else:
            return []

    def get_min(self) -> int:
        if self.min_stack != []:
            return self.min_stack[-1]
        else:
            return []

val = 5
obj = MinStack()
obj.push(val)
obj.pop()
param_3 = obj.top()
param_4 = obj.get_min()
