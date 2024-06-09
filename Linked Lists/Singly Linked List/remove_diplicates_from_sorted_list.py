class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def removeDuplicates(head):
    curr = head
    while curr != None and curr.next != None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
        
    return head

head = Node(10)
head.next = Node(10)
head.next.next = Node(10)
head.next.next.next = Node(10)

# display_linked_list(head)
lst = removeDuplicates(head)
display_linked_list(lst)