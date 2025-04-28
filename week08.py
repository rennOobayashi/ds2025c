
class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def in_order(model):
    if model is None:
        return

    in_order(model.left)
    print(model.data, end='->')
    in_order(model.right)

if __name__ == '__main__':
    numbers = [10, 15, 8, 4, 9]
    root = None

    node = TreeNode()
    node.data = numbers[0]
    root = node

    for i in numbers[1:]:
        n = TreeNode()
        n.data = i

        current = root

        while True:
            if current.data > n.data:
                if current.left is None:
                    current.left = n
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = n
                    break
                else:
                    current = current.right


    in_order(root)

    find_number = int(input())

    c = root

    while True:
        if c is None:
            print(f"cannot find {find_number}")
            break
        elif c.data is find_number:
            print(f"find {find_number}!")
            break
        elif c.data > find_number:
            c = c.left
            continue
        elif c.data < find_number:
            c = c.right
            continue