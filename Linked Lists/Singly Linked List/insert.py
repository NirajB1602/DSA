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

# insertion at beginning 
def insert_at_beginning(head, x):
    temp = Node(x)
    temp.next = head
    return temp
    
# insertion at end 
def insert_at_end(head, x):
    if head == None:
        return Node(x)
    
    curr = head
    while curr.next != None:
        curr = curr.next

    curr.next = Node(x)
    return head

# insertion at any position
def insert_at_any_position(head, x, position):
    temp = Node(x)
    if position <= 0:
        return head
    
    if position == 1:
        temp.next = head
        return temp
    
    curr = head
    for i in range(position - 2):
        curr = curr.next
        if curr == None:
            return head

    temp.next = curr.next
    curr.next = temp
            
    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# lst1 = insert_at_beginning(head, 5)
# display_linked_list(lst1)

# lst2 = insert_at_end(head, 100)
# display_linked_list(lst2)

# lst3 = insert_at_any_position(head, 150, 2)
# lst4 = insert_at_any_position(head, 550, 10)
# display_linked_list(lst3)
# display_linked_list(lst4)

lst5 = insert_at_any_position(head, 200, 0)
display_linked_list(lst5)

# display_linked_list(head)




