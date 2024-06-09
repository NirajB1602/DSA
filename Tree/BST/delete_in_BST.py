class Node:
    def __init__(self, k):
        self.right = None
        self.left = None
        self.key = k

def getSuccessor(root):
    curr = root
    while curr.left != None:
        curr = curr.left

    return curr.key

# recursive solution
def delete(root, k):
    if root == None:
        return None
    
    elif root.key > k:
        root.left = delete(root.left, k)

    elif root.key < k:
        root.right = delete(root.right, k)

    else:
        if root.left == None:
            return root.right
        
        elif root.right == None:
            return root.left
        
        else:
            root.key = getSuccessor(root.right)
            root.right = delete(root.right, root.key)

    return root

root = Node(20)
root.left = Node(15)
root.right = Node(25)
root.left.left = Node(10)
root.left.right = Node(18)

root = delete(root, 10)
root = delete(root, 20)

def is_bst_valid(root, left=float('-inf'), right=float('inf')):
    if root is None:
        return True
    
    if not (left < root.key < right):
        return False

    return (is_bst_valid(root.left, left, root.key) and is_bst_valid(root.right, root.key, right))

print(is_bst_valid(root))





