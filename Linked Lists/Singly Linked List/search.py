class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def search(head, x):
    curr = head
    while curr != None:
        if curr.data == x:
            return 1
        
        curr = curr.next

    return 0

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# display_linked_list(head)
print(search(head, 250))
