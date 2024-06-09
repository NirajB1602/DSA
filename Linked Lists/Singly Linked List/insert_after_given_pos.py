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

# insertion after any position
def insert_after_any_position(head, x, position):
    temp = Node(x)
    curr = head

    if position == 0:
        temp.next = head
        return temp
    
    for i in range(position - 1):
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

lst = insert_after_any_position(head, 200, 4)
display_linked_list(lst)