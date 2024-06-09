class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def count_nodes(head):
    curr = head
    cnt = 0

    while curr != None:
        cnt += 1
        curr = curr.next

    return cnt

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# display_linked_list(head)
print(count_nodes(head))