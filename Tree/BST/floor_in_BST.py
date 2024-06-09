class Node:
    def __init__(self, k):
        self.right = None
        self.left = None
        self.key = k

def getFloor(root, k):
    curr = root
    floor_key = None

    while curr != None:
        if curr.key == k:
            return curr

        elif curr.key > k:
            curr = curr.left

        else:
            floor_key = curr
            curr = curr.right

    return floor_key

# Helper function to print the floor value
def print_floor(root, k):
    result = getFloor(root, k)
    if result is not None:
        print(f"Floor of {k} is {result.key}")
    else:
        print(f"Floor of {k} does not exist in the tree")

root = Node(20)
root.left = Node(15)
root.right = Node(25)
root.left.left = Node(10)
root.left.right = Node(18)

print_floor(root, 16)  
print_floor(root, 13)  
print_floor(root, 20)  
print_floor(root, 5)   
