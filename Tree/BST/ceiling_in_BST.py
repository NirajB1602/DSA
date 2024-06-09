class Node:
    def __init__(self, k):
        self.right = None
        self.left = None
        self.key = k

def getCeil(root, k):
    curr = root
    ceil_key = None

    while curr != None:
        if curr.key == k:
            return curr

        elif curr.key > k:
            ceil_key = curr
            curr = curr.left

        else:
            curr = curr.right

    return ceil_key

# Helper function to print the ceiling value
def print_ceil(root, k):
    result = getCeil(root, k)
    if result is not None:
        print(f"Ceil of {k} is {result.key}")
    else:
        print(f"Ceil of {k} does not exist in the tree")

root = Node(20)
root.left = Node(15)
root.right = Node(25)
root.left.left = Node(10)
root.left.right = Node(18)

print_ceil(root, 16)  
print_ceil(root, 13)  
print_ceil(root, 20)  
print_ceil(root, 5)   
print_ceil(root, 100)
