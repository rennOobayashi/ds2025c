class MyQueue:
    def __init__(self, size):
        self._size = size
        self.rear = -1
        self.front = -1
        self.datas = [None for _ in range(self._size)]

    def getSize(self) -> int:
        return self._size

    def isFull(self) -> bool:
        if self.front == self._size - 1 and self.rear == self.front:
            print("Reset Queue.")
            self.front = -1
            self.rear = -1
        elif self.front == self._size - 1:
            return True
        else:
            return False

    def isEmpty(self) -> bool:
        if self.rear == self.front:
            return True
        else:
            return False

    def enQueue(self, data):
        if self.isFull():
            print("Queue is Full.")
            return
        
        self.front += 1
        self.datas[self.front] = data

    def deQeueue(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        
        self.rear += 1
        data = self.datas[self.rear]
        self.datas[self.rear] = None

        return data

    def Peek(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        
        return self.datas[self.front]

    def PrintQueueDatas(self):
        for i in self.datas:
            print(self.datas[i], end=', ')

        print('end')

q = MyQueue(5)

for i in range(q.getSize()):
    q.enQueue(i)

q.PrintQueueDatas()
print(q.Peek())

for i in range(q.getSize()):    
    q.deQeueue()

q.enQueue(5)
