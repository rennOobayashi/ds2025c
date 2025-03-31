class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head :
            self.head = Node(data)
            return

        current = self.head

        while current.link:
            current = current.link #move current

        current.link = Node(data)


    def __str__(self):
        node = self.head

        datas = ""

        while node is not None:
            datas = datas + str(node.data) + " -> "
            #print(node.data, end=" -> ")
            node = node.link

        return datas + "End Point"
        #return "End Point"

ls = LinkedList()
ls.append(3)
ls.append(2)
ls.append(1)

print(ls)