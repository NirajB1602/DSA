from collections import deque

class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.data = k

def isIdentical(root1, root2):
    if root1 != None and root2 == None or root1 == None and root2 != None:
        return False
    
    q1 = deque()
    q1.append(root1)
    
    q2 = deque()
    q2.append(root2)
    
    while q1 and q2:
        node1 = q1.popleft()
        node2 = q2.popleft()
        
        if node1.data != node2.data:
            return False
            
        if node1.left != None and node2.left == None or node2.left != None and node1.left == None:
            return False
            
        if node1.right != None and node2.right == None or node2.right != None and node1.right == None:
            return False
        
        if node1.left is not None:
            q1.append(node1.left)
            
        if node1.right is not None:
            q1.append(node1.right)
            
        if node2.left is not None:
            q2.append(node2.left)
            
        if node2.right is not None:
            q2.append(node2.right)
            
    if q1 or q2:
        return False
            
    return True

root1 = Node(10)
root1.left = Node(20)
root1.right = Node(30)
root1.right.left = Node(40)
root1.right.right = Node(50)

root2 = Node(10)
root2.left = Node(20)
root2.right = Node(30)
root2.right.left = Node(40)
root2.right.right = Node(50)

print(isIdentical(root1, root2))