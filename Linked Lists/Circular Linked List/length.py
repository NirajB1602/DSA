class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getLength(head):
    if head == None:
        return 0
    
    length = 1
    curr = head.next
    while curr != head:
        curr = curr.next
        length += 1
        
    return length

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

print(getLength(head))