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

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty!")

        self.size -= 1
        temp = self.front
        self.front = self.front.link

        if self.front is None:
            self.rear = None

        temp.link = None

        print(f"dequeue - {temp.data}")

        return temp.data

    def print_queue(self):
        if self.front is None or self.rear is None:
            # front = None, rear = None
            print(self.size, self.front, self.rear)
        else:
            # front = node, rear = node
            print(self.size, self.front.data, self.rear.data)

    def print_queue_data(self):
        data = self.front
        cnt = 0

        while not data is None:
            print(f"{cnt} - {data.data}")
            data = data.link
            cnt += 1

        print()

    def get_rear(self):
        return self.rear.data

    def get_size(self):
        return self.size

q = Queue()
q.enqueue("NayutanSeijin")
q.enqueue("Deco27")
q.enqueue("PinocchioP")
q.enqueue("Maretsu")
q.enqueue("Threee")
q.enqueue("Jin")
q.enqueue("Neru")

q.print_queue_data()

print()
print(q.get_size())
print(q.get_rear())
print()

while q.get_size() > 0:
    q.print_queue()
    q.dequeue()
