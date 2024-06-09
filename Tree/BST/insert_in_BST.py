class Node:
    def __init__(self, k):
        self.right = None
        self.left = None
        self.key = k

# iterative solution
def insert(root, k):
    if root == None:
        return Node(k)

    parent = None
    curr = root
    while curr != None:
        parent = curr

        if curr.key == k:
            return
        
        elif curr.key > k:
            curr = curr.left

        else:
            curr = curr.right

    if parent.key > k:
        parent.left = Node(k)

    else:
        parent.right = Node(k)

    return root

# recursive solution
def rec_insert(root, k):
    if root == None:
        return Node(k)
    
    elif root.key == k:
        return root
    
    elif root.key > k:
        root.left = rec_insert(root.left, k)

    else:
        root.right = rec_insert(root.right, k)

    return root

root = Node(20)
root.left = Node(15)
root.right = Node(25)
root.left.left = Node(10)
root.left.right = Node(18)

insert(root, 5)
insert(root, 8)
insert(root, 50)

def is_bst_valid(root, left=float('-inf'), right=float('inf')):
    if root is None:
        return True
    
    if not (left < root.key < right):
        return False

    return (is_bst_valid(root.left, left, root.key) and is_bst_valid(root.right, root.key, right))

print(is_bst_valid(root))





