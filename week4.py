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

    def search(self, target_data):
        current = self.head

        while current.link:
            if current.data == target_data:
                return True
            current = current.link

        return False

    def search_return_to_string(self, target_data):
        current = self.head

        while current.link:
            if current.data == target_data:
                return "Have"
            current = current.link

        return "Not Have"

    def __str__(self):
        node = self.head

        datas = ""

        while node is not None:
            datas = datas + f"{node.data} -> "
            #print(node.data, end=" -> ")
            node = node.link

        return datas + "End Point"
        #return "End Point"

ls = LinkedList()
ls.append(3)
ls.append(2)
ls.append(1)

print(ls)

print(ls.search(3))
print(ls.search_return_to_string(10))