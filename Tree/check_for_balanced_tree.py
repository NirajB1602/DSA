class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.data = k

def height(root):
    if root == None:
        return 0
    
    else:
        lh = height(root.left)
        rh = height(root.right)
        return max(lh, rh) + 1
            
def isBalanced(root):        
    if root is None:
        return True
            
    l = height(root.left)
    r = height(root.right)
        
    if abs(l - r) > 1:
        return False
        
    return isBalanced(root.left) and isBalanced(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print(isBalanced(root))