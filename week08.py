class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

model1 = TreeNode()
model1.data = 'Nayutan'

model2 = TreeNode()
model2.data = 'Deco*27'
model1.left = model2

model3 = TreeNode()
model3.data = 'Kasamura Tato'
model1.right = model3

model4 = TreeNode()
model4.data = 'MIMI'
model2.left = model4

model5 = TreeNode()
model5.data = 'Threee'
model2.right = model5

model6 = TreeNode()
model6.data = 'PinocchioP'
model3.left = model6

print(model1.left.left.data)