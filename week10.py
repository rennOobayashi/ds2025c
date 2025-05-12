
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

def post_order(model):
    if model is None:
        return

    post_order(model.left)
    post_order(model.right)
    print(model.data, end='->')

def delete_node(node, value):
    if node is None:
        return None

    if value < node.data:
        node.left = delete_node(node.left, value)
    elif value > node.data:
        node.right = delete_node(node.right, value)
    else: #value is node.data
        #only have None or 1 leaf node
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

    return node

if __name__ == '__main__':
    numbers = [10, 15, 8, 4, 9, 14]
    root = None

    node = TreeNode()

    for i in numbers:
        root = node.insert(root, i)

    pre_order(root)
    print()
    in_order(root)
    print()
    post_order(root)
    print()

    #find_number = int(input('enter your number(find): '))
    #print(f"find {find_number}!") if node.search(root, find_number) else print(f"cannot find {find_number}")

    delete_number = int(input('enter your number(delete): '))
    delete_node(root, delete_number)
    post_order(root)
    print()