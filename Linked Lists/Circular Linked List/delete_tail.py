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

def deleteTail(head):
    if head == None:
        return None
        
    elif head.next == head:
        return None
        
    else:
        curr = head
        while curr.next.next != head:
            curr = curr.next
            
        curr.next = head
        return head
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

lst = deleteTail(head)
displayList(lst)