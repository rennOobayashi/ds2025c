import random

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

        # If you do not stop when link is None during append, an error occurs because the next node is connected to None
        while current.link:
            current = current.link #move current

        current.link = Node(data)

    def search(self, target_data):
        current = self.head

        while current:
            if current.data == target_data:
                return True

            current = current.link

        return False

    def search_return_to_string(self, target_data):
        current = self.head

        while current:
            if current.data == target_data:
                return f"Have {target_data}"

            current = current.link

        return f"Not Have {target_data}"

    #This is possible because it is Call by Reference
    def remove_item(self, target_data):
        current = self.head

        # Handle the case where it is the head node first so that it does not link to None
        if current.data == target_data:
            self.head = self.head.link
            return f"Remove {target_data}"

        previous = None

        while current:
            if current.data == target_data:
                previous.link = current.link
                # To solve the problem in doubly linked lists, remove the connection of the removed node
                current.link = None

                return f"Remove {target_data}"

            previous = current
            current = current.link

        return f"Not have {target_data}"

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

#for i in range(10): not use i
# for _ in range(10):
#     r = random.randint(0, 50)
#     ls.append(r)

print(ls)
# print(ls.search_return_to_string(1))

ls.remove_item(2)
ls.remove_item(1)
print(ls)

# print(ls.search(3))
# print(ls.search_return_to_string(10))