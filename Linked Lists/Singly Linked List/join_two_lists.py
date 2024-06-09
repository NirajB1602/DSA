class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def joinTheLists(head1, head2):
    if head1 == None:
        return head2
    
    if head2 == None:
        return head1
    
    curr = head1
    while curr.next != None:
        curr = curr.next
        
    curr.next = head2
    return head1

head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)
head1.next.next.next = Node(40)

# display_linked_list(head)

head2 = Node(100)
head2.next = Node(200)
head2.next.next = Node(300)
head2.next.next.next = Node(400)

lst = joinTheLists(head1, head2)
display_linked_list(lst)

