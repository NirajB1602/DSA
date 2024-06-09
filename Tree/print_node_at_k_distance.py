# Print Node at K distance

class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.key = x
        
        
def printkdist(root,k) :
    if root is None :
        return
    if k == 0 :
        print(root.key,end=" ")
    else :
        printkdist(root.left,k-1)
        printkdist(root,k-1)
        
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

printkdist(root,2)  
