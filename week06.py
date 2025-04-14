class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Queue:
    def __init__(self):
        self.front = None
        self.rear  = None
        self.size = 0

    def enqueue(self, data):
        self.size += 1
        node = Node(data)

        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node

    def dequeue(self) -> str:
        if self.front is None:
            raise IndexError("Queue is empty!")

        self.size -= 1
        temp = self.front
        self.front = self.front.link

        if self.front is None:
            self.rear = None

        temp.link = None

        return f"dequeue - {temp.data}"

    def print_queue(self):
        if self.front is None or self.rear is None:
            print(self.size, self.front, self.rear)
        else:
            print(self.size, self.front.data, self.rear.data)

q = Queue()
q.enqueue("NayutanSeijin")
q.enqueue("Deco27")
q.enqueue("PinocchioP")

print(q.dequeue())
# front = node, rear = node
q.print_queue()

print(q.dequeue())
q.print_queue()

print(q.dequeue())
# front = None, rear = None
q.print_queue()
