class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def sum_nodes(head):
    curr = head
    sum = 0

    while curr != None:
        sum += curr.data
        curr = curr.next

    return sum

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# display_linked_list(head)
print(sum_nodes(head))