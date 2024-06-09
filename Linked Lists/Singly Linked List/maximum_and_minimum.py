class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def maximum(head):
    curr = head
    maxi = curr.data
    while curr != None:
        if curr.data > maxi:
            maxi = curr.data
            
        curr = curr.next
        
    return maxi
    
    
def minimum(head):
    curr = head
    mini = curr.data
    while curr != None:
        if curr.data < mini:
            mini = curr.data
            
        curr = curr.next
    
    return mini


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# display_linked_list(head)
print(maximum(head))
print(minimum(head))