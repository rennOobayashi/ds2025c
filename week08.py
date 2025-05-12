
class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def insert(self, root, value):
        node = TreeNode()
        node.data = value

        if root is None:
            return node

        current = root

        while True:
            if current.data > node.data:
                if current.left is None:
                    current.left = node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                else:
                    current = current.right

        return root

    def search(self, root, find_value) -> bool:
        c = root

        while True:
            if c is None:
                return False
            elif c.data is find_number:
                return True
            elif c.data > find_number:
                c = c.left
                continue
            elif c.data < find_number:
                c = c.right
                continue


def pre_order(model):
    if model is None:
        return

    print(model.data, end='->')
    pre_order(model.left)
    pre_order(model.right)

def in_order(model):
    if model is None:
        return

    in_order(model.left)
    print(model.data, end='->')
    in_order(model.right)

def past_order(model):
    if model is None:
        return

    past_order(model.left)
    past_order(model.right)
    print(model.data, end='->')

if __name__ == '__main__':
    numbers = [10, 15, 8, 4, 9, 1, 7, 100, 5]
    root = None

    node = TreeNode()

    for i in numbers:
        root = node.insert(root, i)

    pre_order(root)
    print()
    in_order(root)
    print()
    past_order(root)
    print()

    find_number = int(input('enter your number: '))

    print(f"find {find_number}!") if node.search(root, find_number) else print(f"cannot find {find_number}")
