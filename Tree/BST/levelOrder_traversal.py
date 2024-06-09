from collections import deque

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def levelOrder(root):
    #code here 
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    
    return result

root = Node(20)
root.left = Node(15)
root.right = Node(25)
root.left.left = Node(10)
root.left.right = Node(18)

print(levelOrder(root))