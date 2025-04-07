class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class Stack:
    def __init__(self):
        self.top = None
        self.index_cnt = 0

    def push(self, data):
        node = Node(data)
        self.index_cnt += 1

        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return print("This stack is empty")

        self.index_cnt -= 1

        popped_node = self.top
        self.top = self.top.link
        popped_node.link = None
        return popped_node.data

    def size(self):
        return self.index_cnt

    def is_empty(self):
        return self.top is None

    def peek(self):
        return self.top.data

s = Stack()
print(s.is_empty())
s.push(1)
print(s.is_empty())
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())