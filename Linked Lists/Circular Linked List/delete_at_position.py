class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def displayList(head):
    if head == None:
        return None
        
    print(head.data)
    curr = head.next
    while curr != head:
        print(curr.data)
        curr = curr.next

def deleteAtPosition(head,pos):
    if head == None:
        return None
        
    elif pos == 1:
        if head.next == head:
            return None
        
        else:
            head.data = head.next.data
            head.next = head.next.next
            return head
            
    else:
        curr = head
        for i in range(pos - 2):
            curr = curr.next
            
        curr.next = curr.next.next
        return head
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

lst = deleteAtPosition(head, 3)
displayList(lst)