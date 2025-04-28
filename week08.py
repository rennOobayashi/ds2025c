def post_order(model):
    if model is None:
        return

    post_order(model.left)
    post_order(model.right)

    print(model.data, end='->')

def in_order(model):
    if model is None:
        return

    in_order(model.left)
    print(model.data, end='->')
    in_order(model.right)

def pre_order(model):
    if model is None:
        return

    print(model.data, end='->')

    pre_order(model.left)
    pre_order(model.right)

class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
node1 = TreeNode()
node1.data = 'Nayutan'

node2 = TreeNode()
node2.data = 'Deco*27'
node1.left = node2

node3 = TreeNode()
node3.data = 'Kasamura Tato'
node1.right = node3

node4 = TreeNode()
node4.data = 'MIMI'
node2.left = node4

node5 = TreeNode()
node5.data = 'Threee'
node2.right = node5

node6 = TreeNode()
node6.data = 'PinocchioP'
node3.left = node6

post_order(node1)
print()
in_order(node1)
print()
pre_order(node1)
print()