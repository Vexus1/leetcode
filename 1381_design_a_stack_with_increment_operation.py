class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            top = self.stack.pop()
            return top
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val

stk = CustomStack(3)
print(stk.push(1))
print(stk.push(2))
print(stk.pop())
print(stk.push(2))
print(stk.push(3))
print(stk.push(4))
print(stk.stack)
print(stk.increment(5, 100))
print(stk.increment(2, 100))
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
