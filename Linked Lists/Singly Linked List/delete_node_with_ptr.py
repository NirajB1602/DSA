class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
    print()

# delete a node when only pointer of the node is given 
def delete_node(ptr):
    temp = ptr.next
    ptr.data = temp.data
    ptr.next = temp.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

delete_node(head)
display_linked_list(head)