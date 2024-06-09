# For every node, data value must be equal to the sum of data values in left and right children. 
# Consider data value as 0 for NULL child.  Also, leaves are considered to follow the property.

from collections import deque

class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.data = k

def isSumProperty(root):
    if root == None:
        return 1
    
    q = deque()
    q.append(root)
    
    while len(q) > 0:
        node = q.popleft()
        
        if node.left == None and node.right == None:
            break
        
        if node.left is not None:
            q.append(node.left)
            left = node.left.data
        else:
            left = 0
            
        if node.right is not None:
            q.append(node.right)
            right = node.right.data
        else:
            right = 0
            
        if node.data != (left + right):
            return 0
            
    return 1

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print(isSumProperty(root))