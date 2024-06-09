class Node:
    def __init__(self, k):
        self.right = None
        self.left = None
        self.data = k

def minValue(root):
    if root == None:
        return -1
        
    if root.left == None:
        return root.data
        
    while root.left != None:
        root = root.left
        
    return root.data

root = Node(20)
root.left = Node(15)
root.right = Node(25)
root.left.left = Node(10)
root.left.right = Node(18)

print(minValue(root))

