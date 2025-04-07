class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[-1]

    def __str__(self):
        return f"{[d for d in self.items]}"

s = Stack()
print(s.is_empty())
s.push(1)
print(s.is_empty())
s.push(2)
s.push(3)
print(s.top())
print(s.pop())
print(s)