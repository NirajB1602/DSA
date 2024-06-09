class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def insert_In_Sorted(head,data):
    temp = Node(data)
    curr = head
    
    if head.data >= data:
        temp.next = head
        return temp
        
    while curr.next != None:
        if curr.next.data >= data:
            break
        
        curr = curr.next
        
    if curr.next != None:
        temp.next = curr.next

    curr.next = temp
    return head


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

lst = insert_In_Sorted(head, 35)
display_linked_list(lst)