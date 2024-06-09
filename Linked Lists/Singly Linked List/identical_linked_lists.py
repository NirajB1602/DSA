class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def areIdentical(head1, head2):
    ptr1 = head1
    ptr2 = head2
    
    while ptr1 != None:
        if ptr1.data != ptr2.data:
            return False
            
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        
    if ptr1 == None and ptr2 == None:
        return True
    
    return False

head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)
head1.next.next.next = Node(40)

head2 = Node(10)
head2.next = Node(20)
head2.next.next = Node(30)
head2.next.next.next = Node(40)

print(areIdentical(head1, head2))

# display_linked_list(head)
