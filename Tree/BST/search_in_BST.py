class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.data = key

# iterative solution
def search(root, key):
    while root != None:
        if root.data == key:
            return True
        
        elif root.data > key:
            root = root.left

        else:
            root = root.right

    return False

# recursive solution 
def rec_search(root, key):
    if root == None:
        return False
    
    elif root.data == key:
        return True
    
    elif root.data > key:
        return rec_search(root.left, key)
    
    else:
        return rec_search(root.right, key)
    
root = Node(20)
root.left = Node(15)
root.right = Node(25)
root.left.left = Node(10)
root.left.right = Node(18)

print(search(root, 18))
print(rec_search(root, 50))