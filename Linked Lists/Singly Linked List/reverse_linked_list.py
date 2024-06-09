class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def reverseList(head):
    stack = []
    curr = head
    while curr != None:
        stack.append(curr.data)
        curr = curr.next
            
    curr = head
    while curr != None:
        curr.data = stack.pop()
        curr = curr.next
            
    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# display_linked_list(head)
lst = reverseList(head)
display_linked_list(lst)